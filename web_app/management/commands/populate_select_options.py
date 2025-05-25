from django.core.management.base import BaseCommand
from web_app.models import SelectCategory, KsatType, SelectOption


class Command(BaseCommand):
    help = 'Populate the database with select options for KSATs'

    def handle(self, *args, **options):
        # Création des catégories de select
        importance_category, _ = SelectCategory.objects.get_or_create(
            name='Importance',
            defaults={'description': 'Niveau d\'importance de la compétence'}
        )
        
        mastery_type1_category, _ = SelectCategory.objects.get_or_create(
            name='Type de maîtrise 1',
            defaults={'description': 'Premier niveau de maîtrise (B, S, M pour Task et Knowledge)'}
        )
        
        mastery_type2_category, _ = SelectCategory.objects.get_or_create(
            name='Type de maîtrise 2',
            defaults={'description': 'Deuxième niveau de maîtrise (1, 2, 3 pour Skill et Ability)'}
        )
        
        mastery_type3_category, _ = SelectCategory.objects.get_or_create(
            name='Type de maîtrise 3',
            defaults={'description': 'Troisième niveau de maîtrise simplifié (1, 2 pour Skill et Ability)'}
        )
        
        # Création des types de KSAT
        task_type, _ = KsatType.objects.get_or_create(name='Task')
        knowledge_type, _ = KsatType.objects.get_or_create(name='Knowledge')
        skill_type, _ = KsatType.objects.get_or_create(name='Skill')
        ability_type, _ = KsatType.objects.get_or_create(name='Ability')
        
        # Options pour l'importance des Task
        task_importance_options = [
            {
                'value': '0',
                'title': 'Aucune compétence requise',
                'description': 'Aucune compétence requise',
                'order': 0
            },
            {
                'value': '1',
                'title': 'Importance 1 (Critique, \'Must have\')',
                'description': ('Importance 1 (Critique, \'Must have\') : \n'
                               'Non-négociable. Le candidat doit être capable d\'accomplir cette tâche au niveau de maîtrise attendu dès l\'affectation sur poste.\n'
                               '---\n'
                               'Le non-respect du niveau cible est généralement rédhibitoire. (candidature non recevable)\n'
                               '---\n'
                               'Raison : La tâche est critique pour le métier ou l\'organisation et ne peut être déléguée ou réalisée à un niveau inférieur. Un candidat sans cette compétence ne serait pas embauché.'),
                'order': 1
            },
            {
                'value': '2',
                'title': 'Importance 2 (Important, mais Acquérable rapidement)',
                'description': ('Importance 2 (Important, mais Acquérable rapidement) : \n'
                               'Le candidat NE doit PAS nécessairement être capable d\'accomplir cette tâche au niveau de maîtrise attendu dès l\'affectation sur poste, à condition de pouvoir le faire dans un délai de ~4 mois. Le candidat peut être embauché avec un niveau inférieur (préciser lequel), mais avec un plan de développement clair.\n'
                               '---\n'
                               'Évaluez le niveau actuel ET le potentiel/la volonté (faisabilité) d\'atteindre le niveau cible.\n'
                               '---\n'
                               'Raison : Le candidat pourrait être opérationnel et maîtriser cette compétence en environ 4 mois. Il s\'agit souvent de compétences techniques ou spécifiques au métier qui peuvent être apprises relativement vite.'),
                'order': 2
            },
            {
                'value': '3',
                'title': 'Importance 3 (Secondaire / Complémentaire/\'Nice to have\')',
                'description': ('Importance 3 (Secondaire / Complémentaire/\'Nice to have\')\n'
                               '---\n'
                               'l\'absence de maîtrise de cette tâche ne fait pas de différence majeure. La maîtrise de cette tâche est un plus (à considérer comme un atout).\n'
                               '---\n'
                               'Raison : L\'absence de cette compétence ne ferait pas une différence significative pour le poste en question. Ces compétences ne sont pas au cœur du métier mais peuvent faciliter les interactions ou créer des ponts avec d\'autres domaines professionnels. Il est d\'ailleurs recommandé d\'inclure environ 5 à 10% de compétences de cette catégorie dans un référentiel.'),
                'order': 3
            },
        ]
        
        # Options pour Type de maîtrise 1 (B,S,M) pour Task
        task_mastery_type1_options = [
            {
                'value': 'B',
                'title': 'Proficiency level BASIC (Notions, Pas encore autonome)',
                'description': ('Proficiency level BASIC\n'
                               '(Notions, Pas encore autonome)\n'
                               '---\n'
                               'Un niveau Basic se rapportant à une tâche (T) correspond en principe à des savoirs (K) de niveau A ou B et des savoir-faire (S, A) de niveau 1 dans les domaines sous-jacents à cette tâche.'),
                'order': 0
            },
            {
                'value': 'S',
                'title': 'Proficiency level SENIOR (Autonome au quotidien)',
                'description': ('Proficiency level SENIOR\n'
                               '(Autonome au quotidien)\n'
                               '---\n'
                               'Un niveau Senior se rapportant à une tâche (T) correspond en principe à des savoirs (K) de niveau C ou D et des savoir-faire (S, A) de niveau 2 dans les domaines sous-jacents à cette tâche.'),
                'order': 1
            },
            {
                'value': 'M',
                'title': 'Proficiency level MASTER (Capable de former)',
                'description': ('Proficiency level MASTER\n'
                               '(Capable de former)\n'
                               '---\n'
                               'Un niveau Master se rapportant à une tâche (T) correspond en principe à des savoirs (K) de niveau E et des savoir-faire (S, A) de niveau 3 dans les domaines sous-jacents à cette tâche.'),
                'order': 2
            },
        ]
        
        # Options pour Type de maîtrise 2 (B,S) pour Task
        task_mastery_type2_options = [
            {
                'value': 'B',
                'title': 'Proficiency level BASIC (Notions, Pas encore autonome)',
                'description': ('Proficiency level BASIC\n'
                               '(Notions, Pas encore autonome)\n'
                               '---\n'
                               'Un niveau Basic se rapportant à une tâche (T) correspond en principe à des savoirs (K) de niveau A ou B et des savoir-faire (S, A) de niveau 1 dans les domaines sous-jacents à cette tâche.'),
                'order': 0
            },
            {
                'value': 'S',
                'title': 'Proficiency level SENIOR (Autonome au quotidien)',
                'description': ('Proficiency level SENIOR\n'
                               '(Autonome au quotidien)\n'
                               '---\n'
                               'Un niveau Senior se rapportant à une tâche (T) correspond en principe à des savoirs (K) de niveau C ou D et des savoir-faire (S, A) de niveau 2 dans les domaines sous-jacents à cette tâche.'),
                'order': 1
            },
        ]
        
        # Options pour l'importance des Skill
        skill_importance_options = [
            {
                'value': '0',
                'title': 'Aucune compétence requise',
                'description': 'Aucune compétence requise',
                'order': 0
            },
            {
                'value': '1',
                'title': 'Importance 1 (Critique, \'Must have\')',
                'description': ('Importance 1 (Critique, \'Must have\') : \n'
                               'Non-négociable. Le candidat doit être en mesure de faire la démonstration de ce SAVOIR (K) au niveau de maîtrise attendu dès l\'affectation sur poste.\n'
                               '---\n'
                               'Le non-respect du niveau cible est généralement rédhibitoire. (candidature non recevable)\n'
                               '---\n'
                               'Raison : Le SAVOIR (K) requis est trop long ou difficile à acquérir pour un candidat qui ne le possède pas. Il peut s\'agir de certaines compétences non techniques (soft skills) fondamentales. Un candidat sans cette compétence ne serait pas embauché.'),
                'order': 1
            },
            {
                'value': '2',
                'title': 'Importance 2 (Important, mais Acquérable rapidement)',
                'description': ('Importance 2 (Important, mais Acquérable rapidement) : \n'
                               'Le candidat NE doit PAS nécessairement être en mesure de faire la démonstration de ce SAVOIR (K) au niveau de maîtrise attendu dès l\'affectation sur poste, à condition de pouvoir le faire dans un délai de  ~4 mois. Le candidat peut être embauché avec un niveau inférieur (préciser lequel), mais avec un plan de développement clair.\n'
                               '---\n'
                               'Évaluez le niveau actuel ET le potentiel/la volonté (faisabilité) d\'atteindre le niveau cible.\n'
                               '---\n'
                               'Raison : Le candidat pourrait être opérationnel et maîtriser cette compétence en environ 4 mois. Il s\'agit souvent de compétences techniques ou spécifiques au métier qui peuvent être apprises relativement vite.'),
                'order': 2
            },
            {
                'value': '3',
                'title': 'Importance 3 (Secondaire / Complémentaire/\'Nice to have\')',
                'description': ('Importance 3 (Secondaire / Complémentaire/\'Nice to have\')\n'
                               '---\n'
                               'l\'absence de maîtrise de cette tâche ne fait pas de différence majeure. La maîtrise de cette tâche est un plus (à considérer comme un atout).\n'
                               '---\n'
                               'Raison : L\'absence de cette compétence ne ferait pas une différence significative pour le poste en question. Ces compétences ne sont pas au cœur du métier mais peuvent faciliter les interactions ou créer des ponts avec d\'autres domaines professionnels. Il est d\'ailleurs recommandé d\'inclure environ 5 à 10% de compétences de cette catégorie dans un référentiel.'),
                'order': 3
            },
        ]
        
        # Options pour Type de maîtrise 2 (1,2,3) pour Skill
        skill_mastery_type2_options = [
            {
                'value': '1',
                'title': 'Must be familiar with this competency',
                'description': 'Must be familiar with this competency (Skill/Ability) and be generally capable of independently handling simple tasks or assignments',
                'order': 0
            },
            {
                'value': '2',
                'title': 'Must be capable of independently handling some complex tasks',
                'description': 'Must be capable of independently handling some complex tasks or assignments related to this competency (Skill/Ability), but may need direction and guidance on others.',
                'order': 1
            },
            {
                'value': '3',
                'title': 'Must be capable of independently handling a wide variety of complex tasks',
                'description': 'Must be capable of independently handling a wide variety of complex and or high profile tasks or assignments related to this competency. Must be an authority in this area and or often sought out by others for advice or to teach/mentor others on highly complex or challenging tasks or assignments related to this competency.',
                'order': 2
            },
        ]
        
        # Options pour Type de maîtrise 3 (1,2) pour Skill
        skill_mastery_type3_options = [
            {
                'value': '1',
                'title': 'Must be familiar with this competency',
                'description': 'Must be familiar with this competency (Skill/Ability) and be generally capable of independently handling simple tasks or assignments',
                'order': 0
            },
            {
                'value': '2',
                'title': 'Must be capable of independently handling some complex tasks',
                'description': 'Must be capable of independently handling some complex tasks or assignments related to this competency (Skill/Ability), but may need direction and guidance on others.',
                'order': 1
            },
        ]
        
        # Copier les options de Skill pour Ability (car similaires)
        ability_importance_options = skill_importance_options
        ability_mastery_type2_options = skill_mastery_type2_options
        ability_mastery_type3_options = skill_mastery_type3_options
        
        # Fonction pour créer les options
        def create_options(ksat_type, category, options_list):
            for option in options_list:
                SelectOption.objects.get_or_create(
                    ksat_type=ksat_type,
                    category=category,
                    value=option['value'],
                    defaults={
                        'title': option['title'],
                        'description': option['description'],
                        'order': option['order']
                    }
                )
                
        # Création des options pour Task
        create_options(task_type, importance_category, task_importance_options)
        create_options(task_type, mastery_type1_category, task_mastery_type1_options)
        create_options(task_type, mastery_type2_category, task_mastery_type2_options)
        
        # Création des options pour Skill
        create_options(skill_type, importance_category, skill_importance_options)
        create_options(skill_type, mastery_type2_category, skill_mastery_type2_options)
        create_options(skill_type, mastery_type3_category, skill_mastery_type3_options)
        
        # Création des options pour Ability
        create_options(ability_type, importance_category, ability_importance_options)
        create_options(ability_type, mastery_type2_category, ability_mastery_type2_options)
        create_options(ability_type, mastery_type3_category, ability_mastery_type3_options)
        
        # Options pour l'importance des Knowledge
        knowledge_importance_options = [
            {
                'value': '0',
                'title': 'Aucune compétence requise',
                'description': 'Aucune compétence requise',
                'order': 0
            },
            {
                'value': '1',
                'title': 'Importance 1 (Critique, \'Must have\')',
                'description': ('Importance 1 (Critique, \'Must have\') : \n'
                               'Non-négociable. Le candidat doit être en mesure de faire la démonstration de ce SAVOIR (K) au niveau de maîtrise attendu dès l\'affectation sur poste.\n'
                               '---\n'
                               'Le non-respect du niveau cible est généralement rédhibitoire. (candidature non recevable)\n'
                               '---\n'
                               'Raison : Le SAVOIR (K) requis est trop long ou difficile à acquérir pour un candidat qui ne le possède pas. Il peut s\'agir de certaines compétences non techniques (soft skills) fondamentales. Un candidat sans cette compétence ne serait pas embauché.'),
                'order': 1
            },
            {
                'value': '2',
                'title': 'Importance 2 (Important, mais Acquérable rapidement)',
                'description': ('Importance 2 (Important, mais Acquérable rapidement) : \n'
                               'Le candidat NE doit PAS nécessairement être en mesure de faire la démonstration de ce SAVOIR (K) au niveau de maîtrise attendu dès l\'affectation sur poste, à condition de pouvoir le faire dans un délai de  ~4 mois. Le candidat peut être embauché avec un niveau inférieur (préciser lequel), mais avec un plan de développement clair.\n'
                               '---\n'
                               'Évaluez le niveau actuel ET le potentiel/la volonté (faisabilité) d\'atteindre le niveau cible.\n'
                               '---\n'
                               'Raison : Le candidat pourrait être opérationnel et maîtriser cette compétence en environ 4 mois. Il s\'agit souvent de compétences techniques ou spécifiques au métier qui peuvent être apprises relativement vite.'),
                'order': 2
            },
            {
                'value': '3',
                'title': 'Importance 3 (Secondaire / Complémentaire/\'Nice to have\')',
                'description': ('Importance 3 (Secondaire / Complémentaire/\'Nice to have\')\n'
                               '---\n'
                               'l\'absence de maîtrise de ce SAVOIR (K) ne fait pas de différence majeure. La maîtrise de ce SAVOIR est un plus (à considérer comme un atout).\n'
                               '---\n'
                               'Raison : L\'absence de cette compétence ne ferait pas une différence significative pour le poste en question. Ces compétences ne sont pas au cœur du métier mais peuvent faciliter les interactions ou créer des ponts avec d\'autres domaines professionnels. Il est d\'ailleurs recommandé d\'inclure environ 5 à 10% de compétences de cette catégorie dans un référentiel.'),
                'order': 3
            },
        ]
        
        # Options pour Type de maîtrise 1 (A,B,C,D) pour Knowledge
        knowledge_mastery_type1_options = [
            {
                'value': 'A',
                'title': 'Level A (Familiarity)',
                'description': ('Level A\n'
                               '(Familiarity)\n'
                               '---\n'
                               'Definition: You can remember previously learned material, recalling facts, basic concepts, terms, and answers.'),
                'order': 0
            },
            {
                'value': 'B',
                'title': 'Level B (Comprehension)',
                'description': ('Level B\n'
                               '(Comprehension)\n'
                               '---\n'
                               'Definition: You can demonstrate understanding of facts and ideas by organizing, comparing, explaining, and describing main ideas.'),
                'order': 1
            },
            {
                'value': 'C',
                'title': 'Level C (Application)',
                'description': ('Level C\n'
                               '(Application)\n'
                               '---\n'
                               'Definition: You can solve problems by applying acquired knowledge, facts, techniques and rules in a different way.'),
                'order': 2
            },
            {
                'value': 'D',
                'title': 'Level D (Analysis & Evaluation)',
                'description': ('Level D\n'
                               '(Analysis & Evaluation)\n'
                               '---\n'
                               'Definition: You can examine and break information into parts by identifying motives or causes. You can make inferences and find evidence to support generalizations. You can present and defend opinions.'),
                'order': 3
            },
        ]
        
        # Options pour Type de maîtrise 2 (A,B,C) pour Knowledge
        knowledge_mastery_type2_options = [
            {
                'value': 'A',
                'title': 'Level A: Can identify basic facts and terms about the subject.',
                'description': 'Level A: Can identify basic facts and terms about the subject.',
                'order': 0
            },
            {
                'value': 'B',
                'title': 'Level B: Can identify relationships of basic facts and state general principles about the subject.',
                'description': 'Level B: Can identify relationships of basic facts and state general principles about the subject.',
                'order': 1
            },
            {
                'value': 'C',
                'title': 'Level C: Can analyze facts and principals and draw conclusions about the subject.',
                'description': 'Level C: Can analyze facts and principals and draw conclusions about the subject.',
                'order': 2
            },
        ]
        
        # Création des options pour Knowledge
        create_options(knowledge_type, importance_category, knowledge_importance_options)
        create_options(knowledge_type, mastery_type1_category, knowledge_mastery_type1_options)
        create_options(knowledge_type, mastery_type2_category, knowledge_mastery_type2_options)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated select options'))
