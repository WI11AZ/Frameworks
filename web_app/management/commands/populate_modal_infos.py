from django.core.management.base import BaseCommand
from web_app.models import ModalInfoCategory, ModalInfo, ModalInfoOption, KsatType


class Command(BaseCommand):
    help = 'Populate the database with modal information texts'

    def handle(self, *args, **options):
        # Création des catégories de modals
        info_button_1, _ = ModalInfoCategory.objects.get_or_create(
            button_id='info-button-1',
            defaults={
                'name': 'Importance',
                'description': 'Informations sur l\'importance des compétences'
            }
        )
        
        info_button_2, _ = ModalInfoCategory.objects.get_or_create(
            button_id='info-button-2',
            defaults={
                'name': 'Type de maîtrise 1',
                'description': 'Informations sur le premier type de maîtrise'
            }
        )
        
        info_button_3, _ = ModalInfoCategory.objects.get_or_create(
            button_id='info-button-3',
            defaults={
                'name': 'Type de maîtrise 2',
                'description': 'Informations sur le deuxième type de maîtrise'
            }
        )
        
        # Récupération des types de KSAT
        task_type = KsatType.objects.get(name='Task')
        knowledge_type = KsatType.objects.get(name='Knowledge')
        skill_type = KsatType.objects.get(name='Skill')
        ability_type = KsatType.objects.get(name='Ability')
        
        # Fonction pour créer les modals et leurs options
        def create_modal_info(category, ksat_type, title, options):
            modal_info, _ = ModalInfo.objects.get_or_create(
                category=category,
                ksat_type=ksat_type,
                defaults={'title': title}
            )
            if title:
                modal_info.title = title
                modal_info.save()
                
            for i, option in enumerate(options):
                ModalInfoOption.objects.get_or_create(
                    modal_info=modal_info,
                    text=option['text'],
                    defaults={
                        'title': option['title'],
                        'order': i
                    }
                )
        
        # Info-button-1 (Importance) pour Skills
        create_modal_info(
            info_button_1, skill_type,
            'Légende de l\'Importance pour Skills (premier select)',
            [
                {'text': '0', 'title': 'Importance 0\nAucune compétence requise'},
                {'text': '1', 'title': 'Importance 1 (Critique, \'Must have\')\nNon-négociable. La compétence est nécessaire dès l\'affectation sur poste.'},
                {'text': '2', 'title': 'Importance 2 (Important mais acquérable rapidement)\nIl s\'agit d\'une compétence importante qui peut être acquise après une courte période d\'adaptation.'},
                {'text': '3', 'title': 'Importance 3 (Secondaire / Complémentaire)\nIl s\'agit d\'une compétence secondaire qui peut être développée avec le temps.'}
            ]
        )
        
        # Info-button-1 (Importance) pour Abilities
        create_modal_info(
            info_button_1, ability_type,
            'Légende de l\'Importance pour Abilities (premier select)',
            [
                {'text': '0', 'title': 'Importance 0\nAucune compétence requise'},
                {'text': '1', 'title': 'Importance 1 (Critique, \'Must have\')\nNon-négociable. La compétence est nécessaire dès l\'affectation sur poste.'},
                {'text': '2', 'title': 'Importance 2 (Important mais acquérable rapidement)\nIl s\'agit d\'une compétence importante qui peut être acquise après une courte période d\'adaptation.'},
                {'text': '3', 'title': 'Importance 3 (Secondaire / Complémentaire)\nIl s\'agit d\'une compétence secondaire qui peut être développée avec le temps.'}
            ]
        )
        
        # Info-button-1 (Importance) pour Knowledge
        create_modal_info(
            info_button_1, knowledge_type,
            'Légende de l\'Importance pour Knowledge (premier select)',
            [
                {'text': '0', 'title': 'Aucune compétence requise'},
                {'text': '1', 'title': 'Importance 1 (Critique, \'Must have\') : \nNon-négociable. Le candidat doit être capable d\'accomplir cette tâche au niveau de maîtrise attendu dès l\'affectation sur poste.\n---\nLe non-respect du niveau cible est généralement rédhibitoire. (candidature non recevable)\n---\nRaison : La compétence est trop longue ou difficile à acquérir pour un candidat qui ne la possède pas. Il peut s\'agir de certaines compétences non techniques (soft skills) fondamentales. Un candidat sans cette compétence ne serait pas embauché.'},
                {'text': '2', 'title': 'Importance 2 (Important, mais Acquérable rapidement) : \nLe candidat NE doit PAS nécessairement être capable d\'accomplir cette tâche au niveau de maîtrise attendu dès l\'affectation sur poste, à condition de pouvoir acquérir les KSA nécessaire dans un délai de  ~4 mois. Le candidat peut être embauché avec un niveau inférieur (préciser lequel), mais avec un plan de développement clair.\n---\nÉvaluez le niveau actuel ET le potentiel/la volonté (faisabilité) d\'atteindre le niveau cible.\n---\nRaison : Le candidat pourrait être opérationnel et maîtriser cette compétence en environ 4 mois. Il s\'agit souvent de compétences techniques ou spécifiques au métier qui peuvent être apprises relativement vite.'},
                {'text': '3', 'title': 'Importance 3 (Secondaire / Complémentaire/\'Nice to have\')\n---\nl\'absence de maîtrise de cette tâche ne fait pas de différence majeure. La maîtrise de cette tâche est un plus (à considérer comme un atout).\n---\nRaison : L\'absence de cette compétence ne ferait pas une différence significative pour le poste en question. Ces compétences ne sont pas au cœur du métier mais peuvent faciliter les interactions ou créer des ponts avec d\'autres domaines professionnels. Il est d\'ailleurs recommandé d\'inclure environ 5 à 10% de compétences de cette catégorie dans un référentiel.'}
            ]
        )
        
        # Info-button-1 (Importance) pour Task
        create_modal_info(
            info_button_1, task_type,
            'Légende de l\'Importance pour Task (premier select)',
            [
                {'text': '0', 'title': 'Aucune compétence requise'},
                {'text': '1', 'title': 'Importance 1 (Critique, \'Must have\') : \nNon-négociable. Le candidat doit être capable d\'accomplir cette tâche au niveau de maîtrise attendu dès l\'affectation sur poste.\n---\nLe non-respect du niveau cible est généralement rédhibitoire. (candidature non recevable)\n---\nRaison : La compétence est trop longue ou difficile à acquérir pour un candidat qui ne la possède pas. Il peut s\'agir de certaines compétences non techniques (soft skills) fondamentales. Un candidat sans cette compétence ne serait pas embauché.'},
                {'text': '2', 'title': 'Importance 2 (Important, mais Acquérable rapidement) : \nLe candidat NE doit PAS nécessairement être capable d\'accomplir cette tâche au niveau de maîtrise attendu dès l\'affectation sur poste, à condition de pouvoir acquérir les KSA nécessaire dans un délai de  ~4 mois. Le candidat peut être embauché avec un niveau inférieur (préciser lequel), mais avec un plan de développement clair.\n---\nÉvaluez le niveau actuel ET le potentiel/la volonté (faisabilité) d\'atteindre le niveau cible.\n---\nRaison : Le candidat pourrait être opérationnel et maîtriser cette compétence en environ 4 mois. Il s\'agit souvent de compétences techniques ou spécifiques au métier qui peuvent être apprises relativement vite.'},
                {'text': '3', 'title': 'Importance 3 (Secondaire / Complémentaire/\'Nice to have\')\n---\nl\'absence de maîtrise de cette tâche ne fait pas de différence majeure. La maîtrise de cette tâche est un plus (à considérer comme un atout).\n---\nRaison : L\'absence de cette compétence ne ferait pas une différence significative pour le poste en question. Ces compétences ne sont pas au cœur du métier mais peuvent faciliter les interactions ou créer des ponts avec d\'autres domaines professionnels. Il est d\'ailleurs recommandé d\'inclure environ 5 à 10% de compétences de cette catégorie dans un référentiel.'}
            ]
        )
        
        # Info-button-2 (Type de maîtrise 1) pour Skills et Abilities
        create_modal_info(
            info_button_2, skill_type,
            'Légende du Type 2 pour Skills (deuxième select)',
            [
                {'text': '1', 'title': 'Level 1 (Basic)\nMust be familiar with this competency (Skill/Ability) and be generally capable of independently handling simple tasks or assignments'},
                {'text': '2', 'title': 'Level 2 (Senior)\nMust be capable of independently handling some complex tasks or assignments related to this competency (Skill/Ability), but may need direction and guidance on others.'},
                {'text': '3', 'title': 'Level 3 (Master)\nMust be capable of independently handling a wide variety of complex and or high profile tasks or assignments related to this competency. Must be an authority in this area and or often sought out by others for advice or to teach/mentor others on highly complex or challenging tasks or assignments related to this competency.'}
            ]
        )
        
        create_modal_info(
            info_button_2, ability_type,
            'Légende du Type 2 pour Abilities (deuxième select)',
            [
                {'text': '1', 'title': 'Level 1 (Basic)\nMust be familiar with this competency (Skill/Ability) and be generally capable of independently handling simple tasks or assignments'},
                {'text': '2', 'title': 'Level 2 (Senior)\nMust be capable of independently handling some complex tasks or assignments related to this competency (Skill/Ability), but may need direction and guidance on others.'},
                {'text': '3', 'title': 'Level 3 (Master)\nMust be capable of independently handling a wide variety of complex and or high profile tasks or assignments related to this competency. Must be an authority in this area and or often sought out by others for advice or to teach/mentor others on highly complex or challenging tasks or assignments related to this competency.'}
            ]
        )
        
        # Info-button-2 (Type de maîtrise 1) pour Knowledge
        create_modal_info(
            info_button_2, knowledge_type,
            'Légende du Type 1 pour Knowledge (deuxième select)',
            [
                {'text': 'A', 'title': 'Level A\n(Familiarity)\n---\nDefinition: You can remember previously learned material, recalling facts, basic concepts, terms, and answers.'},
                {'text': 'B', 'title': 'Level B\n(Comprehension)\n---\nDefinition: You can demonstrate understanding of facts and ideas by organizing, comparing, explaining, and describing main ideas.'},
                {'text': 'C', 'title': 'Level C\n(Application)\n---\nDefinition: You can solve problems by applying acquired knowledge, facts, techniques and rules in a different way.'},
                {'text': 'D', 'title': 'Level D\n(Analysis & Evaluation)\n---\nDefinition: You can examine and break information into parts by identifying motives or causes. You can make inferences and find evidence to support generalizations. You can present and defend opinions.'}
            ]
        )
        
        # Info-button-2 (Type de maîtrise 1) pour Task
        create_modal_info(
            info_button_2, task_type,
            'Légende du Type 1 pour Task (deuxième select)',
            [
                {'text': 'B', 'title': 'Basic proficiency\n(Le profil doit acquérir les connaissances et savoir-faire nécessaires)\n---\nLe profil doit se former (connaissances théoriques et/ou pratiques). Il n\'a pas les compétences requises pour mener la tâche de façon autonome.'},
                {'text': 'S', 'title': 'Senior proficiency\n(Le profil est capable de maîtriser la tâche, sans supervision)\n---\nLe profil est capable de réaliser la tâche de manière autonome, sans supervision, dans le contexte métier et le mandat défini.'},
                {'text': 'M', 'title': 'Master proficiency\n(Le profil est capable de former d\'autres personnes)\n---\nLe profil a une connaissance approfondie dans le domaine ou un niveau de performance lui permettant une maîtrise totale quel que soit le contexte.'}
            ]
        )
        
        # Info-button-3 (Type de maîtrise 2) pour Skills et Abilities
        create_modal_info(
            info_button_3, skill_type,
            'Légende du Type 3 pour Skills (troisième select)',
            [
                {'text': '1', 'title': 'Level 1: Must be familiar with this competency (Skill/Ability) and be generally capable of independently handling simple tasks or assignments'},
                {'text': '2', 'title': 'Level 2: Must be capable of independently handling some complex tasks or assignments related to this competency (Skill/Ability), but may need direction and guidance on others.'}
            ]
        )
        
        create_modal_info(
            info_button_3, ability_type,
            'Légende du Type 3 pour Abilities (troisième select)',
            [
                {'text': '1', 'title': 'Level 1: Must be familiar with this competency (Skill/Ability) and be generally capable of independently handling simple tasks or assignments'},
                {'text': '2', 'title': 'Level 2: Must be capable of independently handling some complex tasks or assignments related to this competency (Skill/Ability), but may need direction and guidance on others.'}
            ]
        )
        
        # Info-button-3 (Type de maîtrise 2) pour Knowledge
        create_modal_info(
            info_button_3, knowledge_type,
            'Légende du Type 2 pour Knowledge (troisième select)',
            [
                {'text': 'A', 'title': 'Level A: Can identify basic facts and terms about the subject.'},
                {'text': 'B', 'title': 'Level B: Can identify relationships of basic facts and state general principles about the subject.'},
                {'text': 'C', 'title': 'Level C: Can analyze facts and principals and draw conclusions about the subject.'}
            ]
        )
        
        # Info-button-3 (Type de maîtrise 2) pour Task
        create_modal_info(
            info_button_3, task_type,
            'Légende du Type 2 pour Task (troisième select)',
            [
                {'text': 'B', 'title': 'Proficiency level BASIC\n(Notions, Pas encore autonome)\n---\nUn niveau Basic se rapportant à une tâche (T) correspond en principe à des savoirs (K) de niveau A ou B et des savoir-faire (S, A) de niveau 1 dans les domaines sous-jacents à cette tâche.'},
                {'text': 'S', 'title': 'Proficiency level SENIOR\n(Autonome au quotidien)\n---\nUn niveau Senior se rapportant à une tâche (T) implique souvent des savoirs (K) de niveau C (voire D) et des savoir-faire (S, A) de niveau 2 (voire 3) dans les domaines sous-jacents à cette tâche.'}
            ]
        )
        
        pass
