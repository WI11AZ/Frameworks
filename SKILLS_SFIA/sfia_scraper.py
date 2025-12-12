import requests
from bs4 import BeautifulSoup
import json
import time
from urllib.parse import urljoin
import re

BASE_URL = "https://sfia-online.org"
FRAMEWORK_URL = f"{BASE_URL}/en/sfia-9/sfia-views/full-framework-view?path=/glance"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7",
    "Referer": BASE_URL,
}

def get_soup(url):
    """Télécharge une page et retourne un objet BeautifulSoup"""
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")

def element_text_with_bullets(el):
    """Retourne le texte en conservant les listes sous forme de puces - item"""
    if el is None:
        return None
    # Convertit explicitement les <li> en lignes avec "- " puis récupère tout le texte
    for li in el.select("li"):
        # Insère un séparateur pour garantir une nouvelle ligne avant/après
        li.insert_before("\n")
        li.insert_after("\n")
    text = el.get_text("\n", strip=True)
    # Ajoute des "- " devant les items de liste si pas déjà présent
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        lines.append(stripped)
    # Déduplique les lignes vides consécutives et joint par double saut de ligne
    return "\n".join(lines)

def collect_text_after_anchor(anchor, stop_anchors):
    """Collecte le texte pertinent (p, ul/ol/li, div) après un ancre jusqu'à la prochaine ancre stop."""
    parts = []
    for node in anchor.next_elements:
        if node is anchor:
            continue
        # Arrêt si on rencontre une autre ancre
        if getattr(node, "name", None) in ["h2","h3","h4","button","span","strong"]:
            text = node.get_text(" ", strip=True) if hasattr(node, 'get_text') else ''
            if any(pat.search(text or "") for pat in stop_anchors):
                break
        if getattr(node, "name", None) in ["p","ul","ol","div","li"]:
            txt = element_text_with_bullets(node)
            if txt:
                parts.append(txt)
    # Nettoyage du texte concaténé
    joined = "\n".join([p for p in parts if p]).strip()
    return joined or None

def extract_definition(soup):
    """Extrait la définition courte du skill (phrase qui commence par un verbe)."""
    # 1) Sélecteurs connus
    definition_el = soup.select_one("div.field-name-field-definition, .sfia-skill-definition")
    if definition_el:
        txt = element_text_with_bullets(definition_el)
        if txt:
            return txt

    # 2) Titre "Definition" puis contenu jusqu'au prochain titre
    heading = soup.find(lambda t: t and getattr(t, 'name', None) in ["h2","h3"] and "Definition" in t.get_text())
    if heading:
        parts = []
        for sib in heading.next_siblings:
            if getattr(sib, "name", None) in ["h2","h3"]:
                break
            if getattr(sib, "name", None) in ["p","div","ul","ol"]:
                txt = element_text_with_bullets(sib)
                if txt:
                    parts.append(txt)
        joined = "\n".join(parts).strip()
        if joined:
            return joined

    # 3) Fallback générique: premiers paragraphes après le H1 jusqu'à "Guidance" ou "Levels"
    h1 = soup.select_one("h1")
    stop_pat = re.compile(r"Guidance notes|Levels of responsibility|Revision notes", re.I)
    if h1:
        parts = []
        for node in h1.next_elements:
            if getattr(node, "name", None) in ["h2","h3"] and stop_pat.search(node.get_text(" ", strip=True) or ""):
                break
            if getattr(node, "name", None) == "p":
                txt = node.get_text(" ", strip=True)
                if txt:
                    parts.append(txt)
            # Arrête une fois qu'on a au moins une phrase raisonnable
            if len(" ".join(parts)) > 120:
                break
        joined = "\n".join(parts).strip()
        if joined:
            return joined

    return None

def get_all_skills():
    """Scrape la page principale et récupère tous les liens vers les skills"""
    soup = get_soup(FRAMEWORK_URL)
    skills = []
    seen_urls = set()

    # Essai 1: structure de tableau attendue
    for a in soup.select("td.views-field-title a"):
        href = a.get("href", "")
        if not href:
            continue
        skill_url = urljoin(BASE_URL, href)
        if skill_url in seen_urls:
            continue
        skill_name = a.text.strip()
        seen_urls.add(skill_url)
        skills.append({"name": skill_name, "url": skill_url})

    # Fallback: tout lien qui ressemble à une page de skill SFIA-9
    if not skills:
        for a in soup.select("a[href*='/en/sfia-9/skills/']"):
            href = a.get("href", "")
            if not href or "#" in href:
                continue
            skill_url = urljoin(BASE_URL, href)
            if skill_url in seen_urls:
                continue
            skill_name = a.text.strip() or skill_url.rsplit("/", 1)[-1]
            seen_urls.add(skill_url)
            skills.append({"name": skill_name, "url": skill_url})

    return skills

def parse_skill_page(url):
    """Scrape la page d’un skill individuel"""
    soup = get_soup(url)
    skill_data = {"url": url}

    # Code + nom
    h1 = soup.select_one("h1")
    if h1:
        h1_text = h1.get_text(" ", strip=True)
        # Essaie d'extraire un code de 3-5 lettres majuscules à la fin
        m = re.search(r"\b([A-Z]{3,5})\b\s*$", h1_text)
        if m:
            skill_data["code"] = m.group(1)
            # Enlève le code du nom s'il est collé à la fin
            name_only = h1_text[:m.start()].strip()
            skill_data["name"] = name_only
        else:
            skill_data["name"] = h1_text
    else:
        skill_data["name"] = None

    # Nom + code combinés pour l'affichage attendu par l'utilisateur
    if skill_data.get("name") and skill_data.get("code"):
        skill_data["name_with_code"] = f"{skill_data['name']} {skill_data['code']}"

    # Définition principale
    definition_text = extract_definition(soup)
    if definition_text:
        skill_data["definition"] = definition_text

    # Guidance note (unique)
    guidance_el = soup.select_one("div.field-name-field-guidance-notes, .sfia-skill-guidance-notes")
    if not guidance_el:
        # Cherche un titre "Guidance notes" puis agrège son contenu jusqu'au prochain titre
        guidance_heading = soup.find(lambda t: t.name in ["h2","h3"] and "Guidance notes" in t.get_text())
        if guidance_heading:
            parts = []
            for sib in guidance_heading.next_siblings:
                if getattr(sib, "name", None) in ["h2","h3"]:
                    break
                if getattr(sib, "name", None) in ["p","ul","ol","div"]:
                    txt = element_text_with_bullets(sib)
                    if txt:
                        parts.append(txt)
            text = "\n".join(parts).strip()
            skill_data["guidance_note"] = text or None
        else:
            skill_data["guidance_note"] = None
    else:
        skill_data["guidance_note"] = element_text_with_bullets(guidance_el)

    # Niveaux
    levels = []
    # Méthode robuste basée sur la présence de "Level X" dans divers types d'éléments
    level_anchor_pattern = re.compile(r"\bLevel\s*([1-7])\b", re.I)
    candidate_headers = []
    for tag_name in ["h2","h3","h4","button","span","strong"]:
        candidate_headers.extend(
            soup.find_all(
                lambda t: getattr(t, 'name', None) == tag_name and level_anchor_pattern.search((t.get_text(" ", strip=True) or ""))
            )
        )

    # Normalise: si l'ancre est un span/strong/button, remonter à son titre parent bloc (h2/h3/h4) si présent
    anchors = []
    for a in candidate_headers:
        header = a
        if a.name in ["span","strong","button"] and a.parent and a.parent.name in ["h2","h3","h4"]:
            header = a.parent
        anchors.append(header)

    # Déduplique par id d'élément et par niveau en préservant l'ordre d'apparition
    seen_nodes = set()
    seen_levels = set()
    deduped = []
    for a in anchors:
        if id(a) in seen_nodes:
            continue
        seen_nodes.add(id(a))
        m = level_anchor_pattern.search(a.get_text(" ", strip=True) or "")
        if not m:
            continue
        lvl = int(m.group(1))
        if lvl in seen_levels:
            continue
        seen_levels.add(lvl)
        deduped.append((lvl, a))

    # Trie par ordre numérique croissant
    deduped.sort(key=lambda x: x[0])

    for lvl, header in deduped:
        title_text = header.get_text(" ", strip=True)
        # Parcourt les frères suivants jusqu'au prochain header de niveau
        parts = []
        for sib in header.next_siblings:
            if getattr(sib, "name", None) in ["h2","h3","h4","button","span","strong"]:
                if level_anchor_pattern.search((sib.get_text(" ", strip=True) if hasattr(sib, 'get_text') else "")):
                    break
            if getattr(sib, "name", None) in ["p","ul","ol","div","section"]:
                txt = element_text_with_bullets(sib)
                if txt:
                    parts.append(txt)
        desc_text = "\n".join(parts).strip() if parts else None

        if skill_data.get("name"):
            formatted_title = f"{skill_data['name']}: Level {lvl}"
        else:
            formatted_title = title_text
        if desc_text:  # ne garder que les niveaux avec contenu
            levels.append({
                "level": lvl,
                "title": formatted_title,
                "definition": desc_text,
            })
    skill_data["levels"] = levels
    return skill_data

def main():
    print("Scraping SFIA framework…")
    all_skills = get_all_skills()
    print(f"Trouvé {len(all_skills)} compétences.")
    results = []

    for i, skill in enumerate(all_skills, 1):
        print(f"[{i}/{len(all_skills)}] {skill['name']}")
        try:
            data = parse_skill_page(skill["url"])
            results.append(data)
        except Exception as e:
            print(f"Erreur sur {skill['name']}: {e}")
        time.sleep(1.5)  # petite pause pour respecter le site

    with open("sfia_skills.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    # Remarque: éviter les emojis qui peuvent poser problème sur Windows (cp1252)
    print("Export terminé : sfia_skills.json")

if __name__ == "__main__":
    main()
