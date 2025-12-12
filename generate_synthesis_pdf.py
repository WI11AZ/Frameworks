#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script pour générer une synthèse complète du projet Frameworks en PDF
"""

from fpdf import FPDF
from datetime import datetime
import os

class PDF(FPDF):
    def header(self):
        # En-tête sur chaque page
        self.set_font('Arial', 'B', 12)
        self.set_text_color(30, 64, 175)  # Bleu
        self.cell(0, 10, 'CyberRoles - ATLAS - Synthèse du Projet', 0, 1, 'C')
        self.ln(5)
    
    def footer(self):
        # Pied de page
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    
    def chapter_title(self, title):
        # Titre de chapitre
        self.set_font('Arial', 'B', 16)
        self.set_text_color(30, 64, 175)  # Bleu foncé
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(3)
    
    def section_title(self, title):
        # Titre de section
        self.set_font('Arial', 'B', 12)
        self.set_text_color(59, 130, 246)  # Bleu moyen
        self.cell(0, 8, title, 0, 1, 'L')
        self.ln(2)
    
    def subsection_title(self, title):
        # Titre de sous-section
        self.set_font('Arial', 'B', 11)
        self.set_text_color(96, 165, 250)  # Bleu clair
        self.cell(0, 7, title, 0, 1, 'L')
        self.ln(1)

def create_synthesis_pdf():
    """Crée un document PDF de synthèse complète du projet"""
    
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Page de titre
    pdf.set_font('Arial', 'B', 24)
    pdf.set_text_color(30, 64, 175)
    pdf.cell(0, 20, 'SYNTHESE COMPLETE DU PROJET', 0, 1, 'C')
    pdf.ln(10)
    
    pdf.set_font('Arial', 'B', 20)
    pdf.set_text_color(59, 130, 246)
    pdf.cell(0, 15, 'CyberRoles - ATLAS', 0, 1, 'C')
    pdf.ln(5)
    
    pdf.set_font('Arial', '', 14)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, 'Framework de Gestion des Compétences Cybersécurité', 0, 1, 'C')
    pdf.ln(20)
    
    pdf.set_font('Arial', 'I', 10)
    pdf.set_text_color(128, 128, 128)
    pdf.cell(0, 10, f'Document généré le {datetime.now().strftime("%d/%m/%Y à %H:%M")}', 0, 1, 'C')
    
    pdf.add_page()
    
    # Table des matières
    pdf.chapter_title("TABLE DES MATIÈRES")
    pdf.ln(5)
    
    toc_items = [
        "1. Vue d'ensemble du projet",
        "2. Architecture technique",
        "3. Frameworks gérés",
        "4. Modèles de données",
        "5. Fonctionnalités principales",
        "6. Technologies utilisées",
        "7. Justification des choix techniques",
        "8. Structure du projet",
        "9. Système d'authentification et rôles",
        "10. Déploiement",
        "11. Conclusion"
    ]
    
    pdf.set_font('Arial', '', 11)
    pdf.set_text_color(0, 0, 0)
    for item in toc_items:
        pdf.cell(0, 8, f"• {item}", 0, 1, 'L')
    
    # ========== 1. VUE D'ENSEMBLE ==========
    pdf.add_page()
    pdf.chapter_title("1. VUE D'ENSEMBLE DU PROJET")
    
    pdf.set_font('Arial', '', 11)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 6, 
        "CyberRoles - ATLAS est une application web Django conçue pour supporter les organisations "
        "dans le mapping systématique de leurs exigences spécifiques—couvrant les connaissances, compétences "
        "techniques et compétences comportementales—associées à chaque poste au sein de la structure organisationnelle.")
    pdf.ln(3)
    
    pdf.multi_cell(0, 6,
        "Ce processus de mapping facilite l'alignement avec les frameworks de référence établis pour la main-d'œuvre "
        "afin d'assurer à la fois l'adéquation des rôles et l'exécution efficace des tâches.")
    pdf.ln(5)
    
    pdf.subsection_title("Objectifs principaux :")
    pdf.set_font('Arial', '', 10)
    
    objectives = [
        "Cartographier les compétences requises pour chaque poste",
        "Comparer et aligner les frameworks DCWF, NCWF et NICE Framework",
        "Faciliter l'identification des rôles de travail (work roles) appropriés",
        "Gérer les compétences KSAT (Knowledge, Skills, Abilities, Tasks)",
        "Fournir des outils d'exploration et de recherche avancés"
    ]
    
    for obj in objectives:
        pdf.cell(10, 6, '', 0, 0)  # Indentation
        pdf.cell(0, 6, f"• {obj}", 0, 1, 'L')
    
    # ========== 2. ARCHITECTURE TECHNIQUE ==========
    pdf.add_page()
    pdf.chapter_title("2. ARCHITECTURE TECHNIQUE")
    
    pdf.set_font('Arial', '', 11)
    pdf.multi_cell(0, 6,
        "Le projet suit une architecture MVC (Model-View-Controller) typique de Django, "
        "avec une séparation claire entre les modèles de données, les vues et les templates.")
    pdf.ln(3)
    
    pdf.subsection_title("Structure principale :")
    pdf.set_font('Arial', '', 10)
    
    architecture_points = [
        "Backend : Django 5.1.6 - Framework web Python robuste et mature",
        "Base de données : SQLite3 pour le développement et la production",
        "Frontend : HTML5, CSS3, JavaScript avec Tailwind CSS pour le styling",
        "Authentification : Système personnalisé basé sur les matricules",
        "API REST : Endpoints JSON pour les données dynamiques"
    ]
    
    for point in architecture_points:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {point}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("Organisation du code :")
    
    code_org = [
        "dcwf/ : Configuration principale Django (settings, urls, wsgi)",
        "web_app/ : Application principale contenant :",
        "  - models/ : Modèles de données (19 fichiers de modèles)",
        "  - views.py, views_auth.py, views_saved_data.py : Logique métier",
        "  - templates/ : Templates HTML organisés par fonctionnalité",
        "  - static/ : Fichiers statiques (CSS, JS, images)",
        "  - management/ : Commandes Django personnalisées",
        "  - helpers/ : Fonctions utilitaires"
    ]
    
    for item in code_org:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {item}", 0, 1, 'L')
    
    # ========== 3. FRAMEWORKS GÉRÉS ==========
    pdf.add_page()
    pdf.chapter_title("3. FRAMEWORKS GÉRÉS")
    
    pdf.set_font('Arial', '', 11)
    pdf.multi_cell(0, 6,
        "L'application gère plusieurs frameworks de compétences cybersécurité, permettant leur comparaison "
        "et leur alignement.")
    pdf.ln(3)
    
    pdf.subsection_title("3.1 DCWF (DoD Cyberspace Workforce Framework)")
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 6,
        "Framework du Département de la Défense américain pour la main-d'œuvre cybersécurité. "
        "Le projet gère deux versions :")
    pdf.ln(2)
    
    dcwf_versions = [
        "DCWF 2017 : Version originale avec 79 work roles",
        "DCWF 2025 : Version mise à jour avec nouvelles catégories et rôles"
    ]
    
    for version in dcwf_versions:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {version}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("3.2 NCWF (NICE Cybersecurity Workforce Framework)")
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 6,
        "Framework NICE (National Initiative for Cybersecurity Education) pour la main-d'œuvre cybersécurité civile. "
        "Le projet gère trois versions :")
    pdf.ln(2)
    
    ncwf_versions = [
        "NCWF 2017 : Version initiale du framework NICE",
        "NCWF 2024 : Version intermédiaire avec améliorations",
        "NCWF 2025 : Version la plus récente avec alignement DCWF 2025"
    ]
    
    for version in ncwf_versions:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {version}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("3.3 NICE Framework")
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 6,
        "Framework NICE standard pour les compétences et rôles cybersécurité, intégré dans les modèles 2025.")
    
    pdf.ln(3)
    pdf.subsection_title("3.4 Mapping entre frameworks")
    pdf.multi_cell(0, 6,
        "Le système maintient des relations entre les work roles des différents frameworks via les OPM IDs "
        "(Occupational Position Matrices), permettant :")
    pdf.ln(2)
    
    mapping_features = [
        "Correspondance automatique entre DCWF et NCWF",
        "Regroupement par OPM ID pour affichage cohérent",
        "Comparaison des KSATs entre frameworks",
        "Visualisation des différences et similitudes"
    ]
    
    for feature in mapping_features:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {feature}", 0, 1, 'L')
    
    # ========== 4. MODÈLES DE DONNÉES ==========
    pdf.add_page()
    pdf.chapter_title("4. MODÈLES DE DONNÉES")
    
    pdf.set_font('Arial', '', 11)
    pdf.multi_cell(0, 6,
        "Le projet utilise 19 modèles Django pour représenter la structure complexe des frameworks.")
    pdf.ln(3)
    
    pdf.subsection_title("4.1 Modèles principaux")
    pdf.set_font('Arial', '', 10)
    
    models_list = [
        "DcwfWorkRole : Rôles de travail DCWF 2017 avec relations OPM",
        "Dcwf2025WorkRole : Rôles de travail DCWF 2025",
        "Ncwf2017WorkRole : Rôles de travail NCWF 2017",
        "Ncwf2024WorkRole : Rôles de travail NCWF 2024",
        "Ncwf2025WorkRole : Rôles de travail NCWF 2025",
        "NiceFrameworkWorkRole : Rôles du framework NICE",
        "AIWorkRole : Rôles spécialisés en Intelligence Artificielle"
    ]
    
    for model in models_list:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {model}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("4.2 Modèles KSAT")
    pdf.multi_cell(0, 6,
        "Les KSATs (Knowledge, Skills, Abilities, Tasks) sont les compétences associées aux work roles :")
    pdf.ln(2)
    
    ksat_models = [
        "DcwfKsat : KSATs DCWF avec catégories (knowledge, skill, ability, task)",
        "Dcwf2025Ksat : KSATs DCWF 2025",
        "Ncwf2017Ksat : KSATs NCWF 2017",
        "Ncwf2024Tks : TKS (Tasks, Knowledge, Skills) NCWF 2024",
        "Ncwf2025Ksat : KSATs NCWF 2025"
    ]
    
    for ksat in ksat_models:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {ksat}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("4.3 Modèles de relations")
    pdf.multi_cell(0, 6,
        "Les relations Many-to-Many sont gérées via des modèles intermédiaires :")
    pdf.ln(2)
    
    relation_models = [
        "DcwfWorkRoleKsatRelation : Relation entre work roles DCWF et KSATs",
        "Dcwf2025WorkRoleKsatRelation : Relations pour DCWF 2025",
        "Ncwf2025WorkRoleKsatRelation : Relations pour NCWF 2025",
        "Opm : Occupational Position Matrix - Point de correspondance entre frameworks"
    ]
    
    for rel in relation_models:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {rel}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("4.4 Modèles utilisateur")
    pdf.multi_cell(0, 6,
        "Le modèle UserSavedData permet de sauvegarder :")
    pdf.ln(2)
    
    user_models = [
        "User : Modèle utilisateur personnalisé avec matricule et rôle",
        "UserSavedData : Données sauvegardées par utilisateur (sélections KSAT, etc.)"
    ]
    
    for user_model in user_models:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {user_model}", 0, 1, 'L')
    
    # ========== 5. FONCTIONNALITÉS PRINCIPALES ==========
    pdf.add_page()
    pdf.chapter_title("5. FONCTIONNALITÉS PRINCIPALES")
    
    pdf.ln(3)
    pdf.subsection_title("5.1 Exploration des Work Roles")
    pdf.set_font('Arial', '', 10)
    
    features_1 = [
        "Page d'accueil (t1.html) : Vue d'ensemble de tous les work roles organisés par catégories",
        "Modèles 2025 : Interface dédiée aux frameworks 2025 avec séparation DCWF/NCWF",
        "Détails work role : Affichage détaillé d'un work role avec ses KSATs",
        "DCWF Finder : Outil interactif avec questionnaire guidé, catalogue complet et recherche rapide"
    ]
    
    for feature in features_1:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {feature}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("5.2 Comparaison de frameworks")
    
    features_2 = [
        "Sélection multi-frameworks : Choix de work roles depuis DCWF 2017, DCWF 2025, NCWF 2017, NCWF 2024, NCWF 2025",
        "Comparaison KSAT : Affichage côte à côte des KSATs avec regroupement par OPM ID",
        "Visualisation par catégories : Organisation par Knowledge, Skills, Abilities, Tasks",
        "Détails de compétences : Pages dédiées pour NF-COM-002 (Sécurité IA) et NF-COM-007 (Cyber Resiliency)"
    ]
    
    for feature in features_2:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {feature}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("5.3 Gestion des compétences (Étape 2)")
    
    features_3 = [
        "Saisie de poste : Interface pour saisir un numéro de poste",
        "Cadres de niveaux : Affichage des cadres de niveaux de maîtrise",
        "Domaines de compétence : Exploration des domaines de compétence NICE Framework (NF-COM)",
        "Sauvegarde : Possibilité de sauvegarder les sélections pour reprise ultérieure",
        "Étape2Plus : Explorateur interactif des domaines de compétence"
    ]
    
    for feature in features_3:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {feature}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("5.4 Outils d'analyse")
    
    features_4 = [
        "Summary Chart : Visualisation graphique des compétences",
        "Summary MIL : Analyse des compétences militaires",
        "Project Recap : Récapitulatif complet du projet",
        "Step0 Baseline : Outil de baseline pour l'analyse initiale"
    ]
    
    for feature in features_4:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {feature}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("5.5 API et données")
    
    features_5 = [
        "API JSON : Endpoints pour récupérer les données KSAT, work roles, etc.",
        "Données externes : Intégration de données SFIA, compétences militaires, postes IDF",
        "Export : Téléchargement de fichiers .md et .mm (FreeMind)"
    ]
    
    for feature in features_5:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {feature}", 0, 1, 'L')
    
    # ========== 6. TECHNOLOGIES UTILISÉES ==========
    pdf.add_page()
    pdf.chapter_title("6. TECHNOLOGIES UTILISÉES")
    
    pdf.ln(3)
    pdf.subsection_title("6.1 Backend")
    pdf.set_font('Arial', '', 10)
    
    backend_tech = [
        "Django 5.1.6 : Framework web Python - Choix justifié par sa maturité, sa sécurité et sa communauté",
        "Python 3.10+ : Langage de programmation principal",
        "SQLite3 : Base de données relationnelle - Simple, portable, suffisante pour ce projet"
    ]
    
    for tech in backend_tech:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {tech}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("6.2 Frontend")
    
    frontend_tech = [
        "HTML5 : Structure sémantique moderne",
        "CSS3 + Tailwind CSS : Framework CSS utilitaire pour un développement rapide et cohérent",
        "JavaScript (Vanilla) : Pas de framework JS lourd - Performance et simplicité",
        "Google Fonts (Inter) : Typographie moderne et lisible"
    ]
    
    for tech in frontend_tech:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {tech}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("6.3 Outils et bibliothèques")
    
    tools = [
        "Django Admin : Interface d'administration intégrée",
        "Django Management Commands : Commandes personnalisées pour la gestion",
        "JSON : Format de données pour les APIs et exports",
        "Excel/CSV : Import/export de données depuis fichiers Excel"
    ]
    
    for tool in tools:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {tool}", 0, 1, 'L')
    
    # ========== 7. JUSTIFICATION DES CHOIX TECHNIQUES ==========
    pdf.add_page()
    pdf.chapter_title("7. JUSTIFICATION DES CHOIX TECHNIQUES")
    
    pdf.ln(3)
    pdf.subsection_title("7.1 Django vs autres frameworks")
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 6, "Pourquoi Django ?", 0, 1, 'L')
    pdf.set_font('Arial', '', 10)
    pdf.ln(2)
    
    django_reasons = [
        "ORM puissant : Facilite la gestion des relations complexes entre frameworks",
        "Admin intégré : Interface d'administration sans développement supplémentaire",
        "Sécurité : Protection CSRF, XSS, SQL injection intégrées",
        "Écosystème : Nombreuses bibliothèques et extensions disponibles",
        "Documentation : Excellente documentation et communauté active",
        "Maturité : Framework stable et éprouvé en production"
    ]
    
    for reason in django_reasons:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {reason}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("7.2 SQLite vs PostgreSQL/MySQL")
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 6, "Pourquoi SQLite ?", 0, 1, 'L')
    pdf.set_font('Arial', '', 10)
    pdf.ln(2)
    
    sqlite_reasons = [
        "Simplicité : Pas de serveur de base de données à configurer",
        "Portabilité : Fichier unique, facile à déplacer et sauvegarder",
        "Suffisance : Volume de données gérable (work roles, KSATs)",
        "Performance : Excellente pour les lectures, suffisante pour ce projet",
        "Déploiement : Simplifie le déploiement sur PythonAnywhere"
    ]
    
    for reason in sqlite_reasons:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {reason}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("7.3 Tailwind CSS vs Bootstrap/CSS custom")
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 6, "Pourquoi Tailwind CSS ?", 0, 1, 'L')
    pdf.set_font('Arial', '', 10)
    pdf.ln(2)
    
    tailwind_reasons = [
        "Développement rapide : Classes utilitaires pour styling immédiat",
        "Cohérence : Design system intégré pour une interface uniforme",
        "Personnalisation : Facile à personnaliser via configuration",
        "Performance : Purge CSS pour réduire la taille finale",
        "Modernité : Approche moderne du styling CSS"
    ]
    
    for reason in tailwind_reasons:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {reason}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("7.4 Architecture modulaire")
    pdf.multi_cell(0, 6,
        "Le projet utilise une architecture modulaire avec séparation des responsabilités :")
    pdf.ln(2)
    
    arch_reasons = [
        "Modèles séparés : Un fichier par modèle pour maintenabilité",
        "Vues spécialisées : views.py, views_auth.py, views_saved_data.py",
        "Templates organisés : Par fonctionnalité (main/, ksat/, work_role/, etc.)",
        "Helpers : Fonctions utilitaires réutilisables",
        "Management commands : Scripts CLI pour administration"
    ]
    
    for reason in arch_reasons:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {reason}", 0, 1, 'L')
    
    # ========== 8. STRUCTURE DU PROJET ==========
    pdf.add_page()
    pdf.chapter_title("8. STRUCTURE DU PROJET")
    
    pdf.ln(3)
    pdf.subsection_title("8.1 Organisation des répertoires")
    pdf.set_font('Arial', '', 10)
    
    structure = [
        "dcwf/ : Configuration Django (settings.py, urls.py, wsgi.py, asgi.py)",
        "web_app/ : Application principale",
        "  ├── models/ : 19 modèles de données",
        "  ├── templates/ : Templates HTML organisés par fonctionnalité",
        "  ├── static/ : Fichiers statiques (CSS, JS, images, outils)",
        "  ├── management/ : Commandes Django personnalisées",
        "  ├── helpers/ : Fonctions utilitaires",
        "  ├── templatetags/ : Tags de template personnalisés",
        "  └── migrations/ : Migrations de base de données",
        "static/ : Fichiers statiques racine",
        "staticfiles/ : Fichiers statiques collectés pour production",
        "KSAT 2025 FINAL/ : Données JSON des frameworks 2025",
        "Step0/ : Outil Baseline",
        "FORSAPINNOEL/ : Données SFIA",
        "SUMAARYMIL/ : Données compétences militaires"
    ]
    
    for item in structure:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {item}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("8.2 Fichiers de configuration")
    
    config_files = [
        "manage.py : Point d'entrée Django",
        "requirements.txt : Dépendances Python (Django ~= 5.1.6)",
        "db.sqlite3 : Base de données SQLite",
        "pythonanywhere_wsgi.py : Configuration WSGI pour PythonAnywhere",
        "deploy_*.py : Scripts de déploiement"
    ]
    
    for config in config_files:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {config}", 0, 1, 'L')
    
    # ========== 9. SYSTÈME D'AUTHENTIFICATION ==========
    pdf.add_page()
    pdf.chapter_title("9. SYSTÈME D'AUTHENTIFICATION ET RÔLES")
    
    pdf.ln(3)
    pdf.subsection_title("9.1 Authentification par matricule")
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 6,
        "Le système utilise une authentification personnalisée basée sur les matricules (7 chiffres) "
        "plutôt que les emails traditionnels, adapté au contexte organisationnel.")
    
    pdf.ln(3)
    pdf.subsection_title("9.2 Système de rôles")
    pdf.multi_cell(0, 6,
        "Trois niveaux de rôles sont définis avec détection automatique :")
    pdf.ln(2)
    
    roles = [
        "Super User : Accès complet, accès direct aux étapes 2 et 3, interface spéciale (bordure violette)",
        "Bêta testeur : Accès étendu, fonctionnalités avancées, interface spéciale (bordure orange)",
        "User Normal : Accès standard, progression normale, interface standard (bordure bleue)"
    ]
    
    for role in roles:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {role}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("9.3 Gestion des données utilisateur")
    pdf.multi_cell(0, 6,
        "Le modèle UserSavedData permet de sauvegarder :")
    pdf.ln(2)
    
    saved_data = [
        "Sélections KSAT (ksat_selection_*)",
        "Données générales utilisateur",
        "Sélections de work roles",
        "Configurations personnalisées"
    ]
    
    for data in saved_data:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {data}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("9.4 Commandes de gestion")
    pdf.multi_cell(0, 6,
        "Commande Django personnalisée manage_user_roles pour :")
    pdf.ln(2)
    
    commands = [
        "Lister tous les rôles",
        "Ajouter/Supprimer des Super Users",
        "Ajouter/Supprimer des Bêta testeurs",
        "Mettre à jour tous les utilisateurs"
    ]
    
    for cmd in commands:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {cmd}", 0, 1, 'L')
    
    # ========== 10. DÉPLOIEMENT ==========
    pdf.add_page()
    pdf.chapter_title("10. DÉPLOIEMENT")
    
    pdf.ln(3)
    pdf.subsection_title("10.1 Plateforme : PythonAnywhere")
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 6,
        "Le projet est déployé sur PythonAnywhere, une plateforme d'hébergement Python "
        "qui simplifie le déploiement Django.")
    
    pdf.ln(3)
    pdf.subsection_title("10.2 Configuration de déploiement")
    
    deploy_config = [
        "URL de production : willaz.pythonanywhere.com",
        "STATIC_ROOT : Configuration spécifique pour PythonAnywhere",
        "ALLOWED_HOSTS : Configuration des hôtes autorisés",
        "WSGI : Configuration WSGI pour servir l'application",
        "Static files : Collecte et configuration des fichiers statiques"
    ]
    
    for config in deploy_config:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {config}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("10.3 Scripts de déploiement")
    
    deploy_scripts = [
        "deploy_willaz.py : Script de déploiement spécifique",
        "deploy_pythonanywhere.py : Script générique PythonAnywhere",
        "deploy_simple.py : Script de déploiement simplifié",
        "deploy_static.py : Script pour fichiers statiques uniquement"
    ]
    
    for script in deploy_scripts:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {script}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("10.4 Documentation de déploiement")
    pdf.multi_cell(0, 6,
        "Plusieurs fichiers de documentation guident le déploiement :")
    pdf.ln(2)
    
    docs = [
        "DEPLOYMENT_GUIDE.md : Guide général de déploiement",
        "PYTHONANYWHERE_DEPLOYMENT.md : Guide spécifique PythonAnywhere",
        "PYTHONANYWHERE_DEPLOYMENT_COMPLETE.md : Guide complet",
        "CONFIGURATION_WILLAZ.md : Configuration spécifique utilisateur",
        "ETAPE2PLUS_PYTHONANYWHERE_DEPLOYMENT.md : Déploiement outil Étape2Plus"
    ]
    
    for doc in docs:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {doc}", 0, 1, 'L')
    
    # ========== 11. CONCLUSION ==========
    pdf.add_page()
    pdf.chapter_title("11. CONCLUSION")
    
    pdf.set_font('Arial', '', 11)
    pdf.multi_cell(0, 6,
        "Le projet CyberRoles - ATLAS représente une solution complète et sophistiquée pour la gestion "
        "et l'alignement des frameworks de compétences cybersécurité.")
    
    pdf.ln(3)
    pdf.subsection_title("Points forts du projet :")
    pdf.set_font('Arial', '', 10)
    
    strengths = [
        "Architecture solide : Django offre une base robuste et maintenable",
        "Gestion multi-frameworks : Support de DCWF, NCWF et NICE Framework avec versions multiples",
        "Interface utilisateur moderne : Tailwind CSS pour une expérience utilisateur agréable",
        "Fonctionnalités complètes : Exploration, comparaison, analyse et sauvegarde",
        "Extensibilité : Architecture modulaire facilitant l'ajout de nouvelles fonctionnalités",
        "Documentation : Documentation complète pour déploiement et utilisation"
    ]
    
    for strength in strengths:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {strength}", 0, 1, 'L')
    
    pdf.ln(3)
    pdf.subsection_title("Utilisations potentielles :")
    
    uses = [
        "Cartographie des compétences organisationnelles",
        "Alignement avec les frameworks de référence",
        "Planification de carrière et développement professionnel",
        "Recrutement et évaluation des compétences",
        "Formation et certification"
    ]
    
    for use in uses:
        pdf.cell(10, 6, '', 0, 0)
        pdf.cell(0, 6, f"• {use}", 0, 1, 'L')
    
    pdf.ln(5)
    pdf.set_font('Arial', '', 11)
    pdf.multi_cell(0, 6,
        "Ce projet démontre une compréhension approfondie des frameworks de compétences cybersécurité "
        "et offre une plateforme puissante pour leur gestion et leur alignement.")
    
    # Sauvegarder le PDF
    output_file = "SYNTHESE_COMPLETE_PROJET_FRAMEWORKS.pdf"
    pdf.output(output_file)
    print(f"PDF généré avec succès : {output_file}")
    return output_file

if __name__ == "__main__":
    try:
        create_synthesis_pdf()
    except Exception as e:
        print(f"Erreur lors de la génération du PDF : {e}")
        import traceback
        traceback.print_exc()
