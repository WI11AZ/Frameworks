import requests
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import urljoin

def extract_four_letters(text):
    """Extrait les 4 lettres en majuscule du h1"""
    # Cherche un pattern de 4 lettres consécutives en majuscule
    match = re.search(r'\b([A-Z]{4})\b', text)
    if match:
        return match.group(1)
    return None

def scrape_generic_attribute(url):
    """Scrape une page d'attribut générique"""
    print(f"Scraping: {url}")
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # h1.documentFirstHeading
    h1 = soup.select_one('h1.documentFirstHeading')
    h1_text_raw = h1.get_text() if h1 else None
    
    # Les 4 lettres en majuscule du h1
    four_letters = extract_four_letters(h1_text_raw) if h1_text_raw else None
    
    # Nettoie le h1 pour enlever les 4 lettres et ne garder que le titre principal
    if h1_text_raw and four_letters:
        # Enlève les 4 lettres et les espaces/sauts de ligne autour
        h1_text = re.sub(r'\s*' + re.escape(four_letters) + r'\s*', '', h1_text_raw).strip()
        # Nettoie les sauts de ligne multiples
        h1_text = re.sub(r'\s+', ' ', h1_text).strip()
    else:
        h1_text = h1_text_raw.strip() if h1_text_raw else None
    
    # p.lead
    lead = soup.select_one('p.lead')
    lead_text = lead.get_text(strip=True) if lead else None
    
    # div.guidance-notes
    guidance_notes = soup.select_one('div.guidance-notes')
    guidance_text = guidance_notes.get_text(strip=True) if guidance_notes else None
    
    # Les h3 skill level avec leur p
    skill_levels = []
    # Cherche toutes les sections avec les skill levels
    # Les h3 peuvent être dans des sections avec id="skill_level_section_X"
    h3_elements = soup.find_all('h3')
    for h3 in h3_elements:
        h3_text = h3.get_text(strip=True)
        # Vérifie si c'est un skill level (commence par "Level" suivi d'un chiffre)
        if re.match(r'^Level\s+\d+', h3_text):
            # Trouve le paragraphe suivant (peut être directement après ou dans la même section)
            p = h3.find_next_sibling('p')
            if not p:
                # Cherche dans le parent ou les éléments suivants
                parent = h3.parent
                if parent:
                    p = parent.find('p')
            p_text = p.get_text(strip=True) if p else None
            skill_levels.append({
                'level': h3_text,
                'description': p_text
            })
    
    return {
        'h1': h1_text,
        'four_letters': four_letters,
        'lead': lead_text,
        'guidance_notes': guidance_text,
        'skill_levels': skill_levels,
        'url': url
    }

def get_all_generic_attributes(base_url):
    """Récupère tous les liens vers les attributs génériques"""
    print(f"Récupération de la liste des attributs depuis: {base_url}")
    response = requests.get(base_url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Trouve aside.portlet.framework-portlet > ul
    aside = soup.select_one('aside.portlet.framework-portlet')
    if not aside:
        print("Avertissement: aside.portlet.framework-portlet non trouvé")
        return []
    
    ul = aside.find('ul')
    if not ul:
        print("Avertissement: ul non trouvé dans l'aside")
        return []
    
    links = []
    for li in ul.find_all('li'):
        a = li.find('a')
        if a and a.get('href'):
            href = a.get('href')
            full_url = urljoin(base_url, href)
            links.append(full_url)
    
    return links

def main():
    # URL de base pour récupérer la liste des attributs
    base_url = "https://sfia-online.org/en/sfia-9/responsibilities/generic-attributes-business-skills-behaviours/autonomy"
    
    # Récupère tous les liens
    all_links = get_all_generic_attributes(base_url)
    
    if not all_links:
        print("Aucun lien trouvé. Tentative avec l'URL de base...")
        # Si on ne trouve pas les liens, on peut essayer de scraper directement
        # ou utiliser une URL de liste
        all_links = [base_url]
    
    print(f"Nombre de pages à scraper: {len(all_links)}")
    
    # Scrape toutes les pages
    results = []
    for link in all_links:
        try:
            data = scrape_generic_attribute(link)
            results.append(data)
        except Exception as e:
            print(f"Erreur lors du scraping de {link}: {e}")
    
    # Sauvegarde en JSON
    output_file = 'sfia_generic_attributes.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\nScraping terminé! {len(results)} pages scrapées.")
    print(f"Résultats sauvegardés dans: {output_file}")
    
    return results

if __name__ == '__main__':
    main()

