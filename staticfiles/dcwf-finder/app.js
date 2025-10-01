// DCWF Work Roles Finder - Application CORRIGÉE avec navigation fonctionnelle

class DCWFApp {
    constructor() {
        this.workRoles = [];
        this.communities = {};
        this.categories = {};
        this.currentMode = null;
        this.currentResults = [];
        this.currentQuestionIndex = 0;
        this.questionnaireAnswers = {};
        this.questions = [];
        
        this.init();
    }

    async init() {
        this.showLoading();
        try {
            await this.loadData();
            this.initializeQuestions();
            this.updateStats();
            this.setupEventListeners();
            console.log(`Application initialisée avec ${this.workRoles.length} work roles`);
            this.validateDataIntegrity();
        } catch (error) {
            console.error('Erreur lors de l\'initialisation:', error);
            alert('Erreur lors du chargement des données. Veuillez recharger la page.');
        } finally {
            this.hideLoading();
        }
    }

    async loadData() {
        try {
            console.log('Chargement des données depuis l\'asset...');
            const response = await fetch('/dcwf-finder/data/');
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const data = await response.json();
            
            // Charger les work roles avec la structure correcte
            this.workRoles = data.work_roles?.map(role => ({
                omp_id: role.omp_id,
                wrl_id: role.wrl_id,
                title: role.title,
                description: role.description,
                dcwf_community: role.dcwf_community,
                ncwf_category: role.ncwf_category,
                keywords: role.keywords || this.generateKeywords(role.title, role.description)
            })) || [];

            // Définir les communautés DCWF complètes
            this.communities = {
                'EN': {
                    name: 'Cyber Enablers',
                    description: 'Personnel qui soutiennent les fonctions cyber-IT, cybersécurité, effets cyberespace à travers la formation, l\'acquisition, le leadership et le support juridique'
                },
                'IT': {
                    name: 'Information Technology',
                    description: 'Personnel qui conçoivent, construisent, configurent, exploitent et maintiennent les systèmes et infrastructures IT'
                },
                'CS': {
                    name: 'Cybersecurity',
                    description: 'Personnel qui sécurisent, défendent et préservent les données, réseaux et systèmes contre les menaces cyber'
                },
                'CI': {
                    name: 'Intel (Cyber)',
                    description: 'Personnel qui collectent, traitent, analysent et diffusent des informations de renseignement cyber'
                },
                'CE': {
                    name: 'Cyber Effects',
                    description: 'Personnel qui planifient, soutiennent et exécutent des capacités d\'effets cyberespace offensifs et défensifs'
                },
                'DA': {
                    name: 'Data/AI',
                    description: 'Personnel qui pilotent et soutiennent les capacités de données, analyse, intelligence artificielle et apprentissage automatique'
                },
                'SE': {
                    name: 'Software Engineering',
                    description: 'Personnel qui gèrent et identifient les spécifications techniques de haut niveau pour développer des logiciels sécurisés'
                },
                'Cx': {
                    name: 'Sans Communauté',
                    description: 'Rôles de travail pas encore attribués à un élément de workforce DCWF spécifique'
                }
            };

            // Définir les catégories NCWF complètes
            this.categories = {
                'OG': {
                    name: 'OVERSIGHT and GOVERNANCE',
                    description: 'Leadership, gestion, direction et plaidoyer pour les capacités et ressources cyber'
                },
                'IN': {
                    name: 'INVESTIGATION',
                    description: 'Enquêtes nationales de cybersécurité et cybercriminalité spécialisées'
                },
                'IO': {
                    name: 'IMPLEMENTATION and OPERATION',
                    description: 'Implémentation, administration, configuration et exploitation des systèmes cyber'
                },
                'DD': {
                    name: 'DESIGN and DEVELOPMENT',
                    description: 'Recherche, conception, développement et test de systèmes et capacités cyber'
                },
                'PD': {
                    name: 'PROTECTION and DEFENSE',
                    description: 'Protection contre et analyse des risques, menaces et vulnérabilités cyber'
                },
                'N/A': {
                    name: 'Hors catégories NCWF',
                    description: 'Work roles sans catégorie NCWF définie ou en cours de classification'
                }
            };
            
            console.log('Données chargées:', {
                workRoles: this.workRoles.length,
                communities: Object.keys(this.communities).length,
                categories: Object.keys(this.categories).length
            });
            
        } catch (error) {
            console.error('Erreur lors du chargement des données:', error);
            throw error;
        }
    }

    generateKeywords(title, description) {
        const text = `${title} ${description}`.toLowerCase();
        const stopWords = new Set([
            'le', 'la', 'les', 'de', 'du', 'des', 'et', 'ou', 'un', 'une', 'dans', 'sur', 'avec', 'pour', 'par',
            'ce', 'qui', 'que', 'est', 'sont', 'avoir', 'être', 'the', 'and', 'or', 'of', 'to', 'in', 'on', 'at',
            'for', 'with', 'by', 'as', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had'
        ]);

        return text
            .replace(/[.,;:!?()"-]/g, ' ')
            .split(/\s+/)
            .map(word => word.trim())
            .filter(word => word.length > 2 && !stopWords.has(word))
            .filter(word => !/^\d+$/.test(word))
            .slice(0, 15); // Limiter à 15 mots-clés
    }

    validateDataIntegrity() {
        console.log('=== VALIDATION DE L\'INTÉGRITÉ DES DONNÉES ===');
        
        // Statistiques par communauté
        const communityStats = {};
        Object.keys(this.communities).forEach(key => {
            communityStats[key] = this.workRoles.filter(role => role.dcwf_community === key).length;
        });
        
        // Statistiques par catégorie
        const categoryStats = {};
        Object.keys(this.categories).forEach(key => {
            categoryStats[key] = this.workRoles.filter(role => role.ncwf_category === key).length;
        });
        
        console.log('Répartition par communauté DCWF:', communityStats);
        console.log('Répartition par catégorie NCWF:', categoryStats);
        
        // Vérifier qu'aucune catégorie n'est vide
        const emptyCommunities = Object.entries(communityStats).filter(([key, count]) => count === 0);
        const emptyCategories = Object.entries(categoryStats).filter(([key, count]) => count === 0);
        
        if (emptyCommunities.length > 0) {
            console.warn('⚠️ Communautés vides:', emptyCommunities);
        } else {
            console.log('✅ Toutes les communautés DCWF ont des work roles');
        }
        
        if (emptyCategories.length > 0) {
            console.warn('⚠️ Catégories vides:', emptyCategories);
        } else {
            console.log('✅ Toutes les catégories NCWF ont des work roles');
        }
        
        // Validation spéciale pour PD (doit avoir 7 work roles)
        const pdRoles = this.workRoles.filter(role => role.ncwf_category === 'PD');
        console.log(`Catégorie PD: ${pdRoles.length} work roles`, pdRoles.map(r => `${r.omp_id} - ${r.title}`));
        
        console.log(`Total work roles chargés: ${this.workRoles.length}`);
    }

    initializeQuestions() {
        this.questions = [
            {
                id: 'q1',
                text: 'Quel est votre domaine d\'activité principal ?',
                options: [
                    { value: 'management', label: '👔 Management et Leadership' },
                    { value: 'security', label: '🛡️ Cybersécurité et Protection' },
                    { value: 'technical', label: '⚙️ Technique et Opérationnel' },
                    { value: 'development', label: '💻 Développement et Conception' },
                    { value: 'data', label: '📊 Données et Intelligence' },
                    { value: 'support', label: '🎓 Formation et Support' },
                    { value: 'investigation', label: '🔍 Investigation et Enquête' },
                    { value: 'other', label: '🌐 Autre domaine' }
                ]
            },
            {
                id: 'q2',
                text: 'Dans quel environnement travaillez-vous ?',
                options: [
                    { value: 'cybersecurity', label: 'Cybersécurité et défense' },
                    { value: 'it_systems', label: 'Systèmes informatiques et IT' },
                    { value: 'software', label: 'Développement logiciel' },
                    { value: 'data_ai', label: 'Données et Intelligence Artificielle' },
                    { value: 'cyber_effects', label: 'Effets cyber et opérations' },
                    { value: 'mixed', label: 'Environnement mixte ou généraliste' }
                ]
            },
            {
                id: 'q3',
                text: 'Quel est votre niveau de responsabilité ?',
                options: [
                    { value: 'strategic', label: 'Stratégique - Direction et gouvernance' },
                    { value: 'management', label: 'Management - Gestion d\'équipe' },
                    { value: 'expert', label: 'Expert - Spécialisation technique' },
                    { value: 'operational', label: 'Opérationnel - Exécution et mise en œuvre' },
                    { value: 'support', label: 'Support - Assistance et formation' }
                ]
            },
            {
                id: 'q4',
                text: 'Quelle est votre expérience dans le domaine cyber ?',
                options: [
                    { value: 'expert', label: 'Expert (5+ ans) - Leadership et stratégie' },
                    { value: 'experienced', label: 'Expérimenté (2-5 ans) - Autonomie complète' },
                    { value: 'intermediate', label: 'Intermédiaire (6 mois-2 ans) - Supervision partielle' },
                    { value: 'beginner', label: 'Débutant (<6 mois) - Formation et encadrement' }
                ]
            }
        ];
    }

    setupEventListeners() {
        console.log('Configuration des event listeners...');
        
        // Menu principal - CORRECTION CRITIQUE
        const menuCards = document.querySelectorAll('.menu-card');
        menuCards.forEach(card => {
            const mode = card.dataset.mode;
            console.log(`Configuring menu card: ${mode}`);
            
            // Supprimer les anciens listeners
            const newCard = card.cloneNode(true);
            card.parentNode.replaceChild(newCard, card);
            
            newCard.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                console.log(`Menu card clicked: ${mode}`);
                this.switchToMode(mode);
            });
        });

        // Retour au menu - CORRECTION CRITIQUE
        this.setupBackToMenuButton();
        this.setupQuestionnaireButtons();
        this.setupCatalogTabs();
        this.setupSearchControls();
        this.setupRecommendationsControls();
        this.setupModalControls();
        this.setupExportControls();
        this.setupLogoNavigation();
        
        console.log('Event listeners configurés avec succès');
    }

    setupBackToMenuButton() {
        const backButton = document.getElementById('back-to-menu');
        if (backButton) {
            // CORRECTION: Créer un nouveau bouton pour éviter les conflits
            const newBackButton = backButton.cloneNode(true);
            backButton.parentNode.replaceChild(newBackButton, backButton);
            
            newBackButton.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                console.log('Back to menu button clicked');
                this.showMainMenu();
            });
            
            console.log('Back to menu button configured');
        }
    }

    setupQuestionnaireButtons() {
        const nextBtn = document.getElementById('next-btn');
        const prevBtn = document.getElementById('prev-btn');
        
        if (nextBtn) {
            const newNextBtn = nextBtn.cloneNode(true);
            nextBtn.parentNode.replaceChild(newNextBtn, nextBtn);
            
            newNextBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                console.log('Next button clicked');
                this.nextQuestion();
            });
        }
        
        if (prevBtn) {
            const newPrevBtn = prevBtn.cloneNode(true);
            prevBtn.parentNode.replaceChild(newPrevBtn, prevBtn);
            
            newPrevBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                console.log('Previous button clicked');
                this.prevQuestion();
            });
        }
        
        console.log('Questionnaire buttons configured');
    }

    setupCatalogTabs() {
        const catalogTabs = document.querySelectorAll('.catalog-tab');
        catalogTabs.forEach(tab => {
            const newTab = tab.cloneNode(true);
            tab.parentNode.replaceChild(newTab, tab);
            
            newTab.addEventListener('click', (e) => {
                e.preventDefault();
                const view = e.target.dataset.view;
                console.log('Catalog tab clicked:', view);
                this.switchCatalogView(view);
            });
        });
    }

    setupSearchControls() {
        const searchInput = document.getElementById('search-input');
        const searchBtn = document.getElementById('search-btn');
        const communityFilter = document.getElementById('community-filter');
        const categoryFilter = document.getElementById('category-filter');
        const sortSelect = document.getElementById('sort-select');
        
        if (searchInput) {
            searchInput.addEventListener('input', () => {
                clearTimeout(this.searchTimeout);
                this.searchTimeout = setTimeout(() => this.performSearch(), 300);
            });
        }
        
        if (searchBtn) {
            searchBtn.addEventListener('click', (e) => {
                e.preventDefault();
                this.performSearch();
            });
        }
        
        [communityFilter, categoryFilter, sortSelect].forEach(element => {
            if (element) {
                element.addEventListener('change', () => {
                    if (element === sortSelect) {
                        this.sortResults(element.value);
                    } else {
                        this.performSearch();
                    }
                });
            }
        });
    }

    setupRecommendationsControls() {
        const analyzeBtn = document.getElementById('analyze-btn');
        if (analyzeBtn) {
            analyzeBtn.addEventListener('click', (e) => {
                e.preventDefault();
                this.getRecommendations();
            });
        }
    }

    setupModalControls() {
        const modalClose = document.getElementById('modal-close');
        if (modalClose) {
            modalClose.addEventListener('click', (e) => {
                e.preventDefault();
                this.closeModal();
            });
        }
    }

    setupExportControls() {
        const exportBtn = document.getElementById('export-btn');
        if (exportBtn) {
            exportBtn.addEventListener('click', (e) => {
                e.preventDefault();
                this.exportResults();
            });
        }
    }

    setupLogoNavigation() {
        const logoTitle = document.querySelector('.logo-title');
        if (logoTitle) {
            logoTitle.style.cursor = 'pointer';
            logoTitle.addEventListener('click', (e) => {
                e.preventDefault();
                this.showMainMenu();
            });
        }
    }

    showMainMenu() {
        console.log('Showing main menu');
        
        const mainMenu = document.getElementById('main-menu');
        const appContent = document.getElementById('app-content');
        const resultsSection = document.getElementById('results-section');
        
        if (mainMenu) mainMenu.style.display = 'block';
        if (appContent) appContent.style.display = 'none';
        if (resultsSection) resultsSection.style.display = 'none';
        
        this.currentMode = null;
        this.currentResults = [];
        this.currentQuestionIndex = 0;
        this.questionnaireAnswers = {};
        
        console.log('Main menu displayed successfully');
    }

    switchToMode(mode) {
        console.log(`Switching to mode: ${mode}`);
        
        const mainMenu = document.getElementById('main-menu');
        const appContent = document.getElementById('app-content');
        
        if (mainMenu) mainMenu.style.display = 'none';
        if (appContent) appContent.style.display = 'block';
        
        // Masquer toutes les sections
        document.querySelectorAll('.mode-section').forEach(section => {
            section.classList.remove('active');
        });
        
        // Afficher la section correspondante
        const targetSection = document.getElementById(`${mode}-mode`);
        if (targetSection) {
            targetSection.classList.add('active');
            console.log(`Section ${mode}-mode activated`);
        } else {
            console.error(`Section ${mode}-mode not found`);
        }
        
        this.currentMode = mode;
        const resultsSection = document.getElementById('results-section');
        if (resultsSection) resultsSection.style.display = 'none';

        // Initialiser le mode spécifique
        switch (mode) {
            case 'questionnaire':
                this.initializeQuestionnaire();
                break;
            case 'catalog':
                this.initializeCatalog();
                break;
            case 'search':
                this.initializeSearch();
                break;
            case 'recommendations':
                this.initializeRecommendations();
                break;
        }
        
        console.log(`Mode ${mode} activated successfully`);
    }

    // Questionnaire Mode
    initializeQuestionnaire() {
        console.log('Initializing questionnaire');
        this.currentQuestionIndex = 0;
        this.questionnaireAnswers = {};
        
        const totalQuestionsEl = document.getElementById('total-questions');
        if (totalQuestionsEl) {
            totalQuestionsEl.textContent = this.questions.length;
        }
        
        this.renderQuestion();
    }

    renderQuestion() {
        const question = this.questions[this.currentQuestionIndex];
        if (!question) {
            console.error('No question found at index:', this.currentQuestionIndex);
            return;
        }

        console.log(`Rendering question ${this.currentQuestionIndex + 1}: ${question.text}`);

        const questionTextEl = document.getElementById('question-text');
        const currentQuestionEl = document.getElementById('current-question');
        const optionsContainer = document.getElementById('question-options');
        
        if (questionTextEl) questionTextEl.textContent = question.text;
        if (currentQuestionEl) currentQuestionEl.textContent = this.currentQuestionIndex + 1;

        if (optionsContainer) {
            optionsContainer.innerHTML = '';

            question.options.forEach(option => {
                const button = document.createElement('button');
                button.className = 'question-option';
                button.textContent = option.label;
                button.dataset.value = option.value;
                
                if (this.questionnaireAnswers[question.id] === option.value) {
                    button.classList.add('selected');
                }
                
                button.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    this.selectOption(option.value);
                });
                
                optionsContainer.appendChild(button);
            });
        }

        // Mettre à jour la barre de progression
        const progressFill = document.getElementById('progress-fill');
        if (progressFill) {
            const progress = ((this.currentQuestionIndex + 1) / this.questions.length) * 100;
            progressFill.style.width = `${progress}%`;
        }

        this.updateQuestionUI();
    }

    selectOption(value) {
        const question = this.questions[this.currentQuestionIndex];
        this.questionnaireAnswers[question.id] = value;
        console.log(`Option selected: ${value} for question ${question.id}`);

        document.querySelectorAll('.question-option').forEach(btn => {
            btn.classList.remove('selected');
            if (btn.dataset.value === value) {
                btn.classList.add('selected');
            }
        });
        
        this.updateQuestionUI();
    }

    updateQuestionUI() {
        const question = this.questions[this.currentQuestionIndex];
        const hasAnswer = this.questionnaireAnswers[question.id];
        
        const prevBtn = document.getElementById('prev-btn');
        const nextBtn = document.getElementById('next-btn');
        
        if (prevBtn) prevBtn.disabled = this.currentQuestionIndex === 0;
        if (nextBtn) nextBtn.disabled = !hasAnswer;
        
        if (nextBtn) {
            if (this.currentQuestionIndex === this.questions.length - 1) {
                nextBtn.textContent = 'Voir les résultats';
            } else {
                nextBtn.textContent = 'Suivant';
            }
        }
    }

    nextQuestion() {
        console.log(`Next question - current index: ${this.currentQuestionIndex}`);
        
        if (this.currentQuestionIndex < this.questions.length - 1) {
            this.currentQuestionIndex++;
            this.renderQuestion();
        } else {
            console.log('End of questionnaire - processing results');
            this.processQuestionnaireResults();
        }
    }

    prevQuestion() {
        console.log(`Previous question - current index: ${this.currentQuestionIndex}`);
        
        if (this.currentQuestionIndex > 0) {
            this.currentQuestionIndex--;
            this.renderQuestion();
        }
    }

    processQuestionnaireResults() {
        const results = this.filterWorkRolesByAnswers();
        this.currentResults = results.slice(0, 10); // Top 10
        this.showResults();
    }

    filterWorkRolesByAnswers() {
        let scoredRoles = this.workRoles.map(role => {
            let score = 0;
            
            Object.entries(this.questionnaireAnswers).forEach(([questionId, answer]) => {
                score += this.calculateQuestionnaireScore(role, questionId, answer);
            });
            
            return { ...role, questionnaireScore: score };
        });

        return scoredRoles
            .filter(role => role.questionnaireScore > 0)
            .sort((a, b) => b.questionnaireScore - a.questionnaireScore);
    }

    calculateQuestionnaireScore(role, questionId, answer) {
        let score = 0;
        const keywords = role.keywords.map(k => k.toLowerCase());
        const description = role.description.toLowerCase();
        const title = role.title.toLowerCase();

        switch (questionId) {
            case 'q1': // Domaine principal
                switch (answer) {
                    case 'management':
                        if (role.ncwf_category === 'OG' || keywords.some(k => ['manager', 'leadership', 'program', 'oversight'].includes(k))) score += 10;
                        break;
                    case 'security':
                        if (['CS', 'CE'].includes(role.dcwf_community) || keywords.some(k => ['cyber', 'security', 'defense', 'protection'].includes(k))) score += 10;
                        break;
                    case 'technical':
                        if (['IT', 'SE'].includes(role.dcwf_community) || role.ncwf_category === 'IO' || keywords.some(k => ['technical', 'systems', 'implementation'].includes(k))) score += 10;
                        break;
                    case 'development':
                        if (role.dcwf_community === 'SE' || role.ncwf_category === 'DD' || keywords.some(k => ['development', 'software', 'design'].includes(k))) score += 10;
                        break;
                    case 'data':
                        if (['DA', 'CI'].includes(role.dcwf_community) || keywords.some(k => ['data', 'intelligence', 'analysis'].includes(k))) score += 10;
                        break;
                    case 'support':
                        if (role.dcwf_community === 'EN' || keywords.some(k => ['training', 'education', 'support'].includes(k))) score += 10;
                        break;
                    case 'investigation':
                        if (role.ncwf_category === 'IN' || keywords.some(k => ['investigation', 'forensic', 'incident'].includes(k))) score += 10;
                        break;
                }
                break;
                
            case 'q2': // Environnement
                switch (answer) {
                    case 'cybersecurity':
                        if (['CS', 'CE'].includes(role.dcwf_community)) score += 8;
                        break;
                    case 'it_systems':
                        if (role.dcwf_community === 'IT') score += 8;
                        break;
                    case 'software':
                        if (role.dcwf_community === 'SE') score += 8;
                        break;
                    case 'data_ai':
                        if (['DA', 'CI'].includes(role.dcwf_community)) score += 8;
                        break;
                    case 'cyber_effects':
                        if (role.dcwf_community === 'CE') score += 8;
                        break;
                }
                break;
                
            case 'q3': // Niveau de responsabilité
                switch (answer) {
                    case 'strategic':
                        if (role.ncwf_category === 'OG' || keywords.some(k => ['manager', 'program', 'strategic'].includes(k))) score += 6;
                        break;
                    case 'management':
                        if (keywords.some(k => ['manager', 'lead', 'program'].includes(k))) score += 6;
                        break;
                    case 'expert':
                        if (keywords.some(k => ['specialist', 'analyst', 'architect'].includes(k))) score += 6;
                        break;
                    case 'operational':
                        if (role.ncwf_category === 'IO' || keywords.some(k => ['operations', 'implementation', 'maintenance'].includes(k))) score += 6;
                        break;
                    case 'support':
                        if (role.dcwf_community === 'EN' || keywords.some(k => ['support', 'training'].includes(k))) score += 6;
                        break;
                }
                break;
                
            case 'q4': // Expérience
                // Score bonus basé sur la complexité du rôle
                if (answer === 'expert' && (role.ncwf_category === 'OG' || keywords.some(k => ['architect', 'manager'].includes(k)))) score += 4;
                else if (answer === 'experienced' && keywords.some(k => ['analyst', 'specialist'].includes(k))) score += 4;
                else if (answer === 'intermediate' && keywords.some(k => ['support', 'technician'].includes(k))) score += 4;
                else if (answer === 'beginner' && keywords.some(k => ['trainee', 'junior', 'assistant'].includes(k))) score += 4;
                break;
        }

        return score;
    }

    // Catalog Mode
    initializeCatalog() {
        console.log('Initializing catalog');
        this.renderCommunities();
        this.renderCategories();
    }

    switchCatalogView(view) {
        console.log('Switching catalog view to:', view);
        
        document.querySelectorAll('.catalog-tab').forEach(tab => {
            tab.classList.remove('active');
        });
        
        const activeTab = document.querySelector(`[data-view="${view}"]`);
        if (activeTab) activeTab.classList.add('active');

        document.querySelectorAll('.catalog-view').forEach(viewElement => {
            viewElement.classList.remove('active');
        });
        
        const activeView = document.getElementById(`${view}-view`);
        if (activeView) activeView.classList.add('active');
    }

    renderCommunities() {
        const container = document.getElementById('communities-list');
        if (!container) return;

        console.log('Rendering communities');
        container.innerHTML = '';

        Object.entries(this.communities).forEach(([key, community]) => {
            const roles = this.workRoles.filter(role => role.dcwf_community === key);
            const section = this.createCatalogSection(key, community.name, community.description, roles);
            container.appendChild(section);
        });
    }

    renderCategories() {
        const container = document.getElementById('categories-list');
        if (!container) return;

        console.log('Rendering categories');
        container.innerHTML = '';

        Object.entries(this.categories).forEach(([key, category]) => {
            const roles = this.workRoles.filter(role => role.ncwf_category === key);
            const section = this.createCatalogSection(key, category.name, category.description, roles);
            container.appendChild(section);
        });
    }

    createCatalogSection(key, name, description, roles) {
        const section = document.createElement('div');
        section.className = 'catalog-section';
        
        section.innerHTML = `
            <div class="catalog-section-header">
                <h4 class="catalog-section-title">${name}</h4>
                <span class="catalog-section-count">${roles.length}</span>
            </div>
            <div class="catalog-section-content">
                <p class="catalog-section-description">${description}</p>
                <div class="catalog-roles"></div>
            </div>
        `;

        const rolesContainer = section.querySelector('.catalog-roles');
        roles.forEach(role => {
            const card = this.createWorkRoleCard(role);
            rolesContainer.appendChild(card);
        });

        section.querySelector('.catalog-section-header').addEventListener('click', () => {
            section.classList.toggle('expanded');
        });

        return section;
    }

    // Search Mode
    initializeSearch() {
        console.log('Initializing search');
        this.setupSearchFilters();
        this.performSearch(); // Afficher tous les résultats initialement
    }

    setupSearchFilters() {
        const communityFilter = document.getElementById('community-filter');
        const categoryFilter = document.getElementById('category-filter');

        if (communityFilter) {
            communityFilter.innerHTML = '<option value="">Toutes les communautés</option>';
            Object.entries(this.communities).forEach(([key, community]) => {
                const option = document.createElement('option');
                option.value = key;
                option.textContent = community.name;
                communityFilter.appendChild(option);
            });
        }

        if (categoryFilter) {
            categoryFilter.innerHTML = '<option value="">Toutes les catégories</option>';
            Object.entries(this.categories).forEach(([key, category]) => {
                const option = document.createElement('option');
                option.value = key;
                option.textContent = category.name;
                categoryFilter.appendChild(option);
            });
        }
    }

    performSearch() {
        const searchInput = document.getElementById('search-input');
        const communityFilter = document.getElementById('community-filter');
        const categoryFilter = document.getElementById('category-filter');
        
        const query = searchInput ? searchInput.value.toLowerCase() : '';
        const communityFilterValue = communityFilter ? communityFilter.value : '';
        const categoryFilterValue = categoryFilter ? categoryFilter.value : '';

        console.log('Performing search:', { query, communityFilterValue, categoryFilterValue });

        let results = [...this.workRoles];

        // Filtrer par requête de recherche
        if (query.length >= 1) {
            results = results.filter(role => {
                const searchText = [
                    role.title,
                    role.description,
                    ...role.keywords,
                    this.communities[role.dcwf_community]?.name || '',
                    this.categories[role.ncwf_category]?.name || ''
                ].join(' ').toLowerCase();

                return searchText.includes(query);
            });
        }

        // Filtrer par communauté
        if (communityFilterValue) {
            results = results.filter(role => role.dcwf_community === communityFilterValue);
        }

        // Filtrer par catégorie
        if (categoryFilterValue) {
            results = results.filter(role => role.ncwf_category === categoryFilterValue);
        }

        console.log(`Search results: ${results.length} roles`);
        this.currentResults = results;
        this.showResults();
    }

    sortResults(criteria) {
        switch (criteria) {
            case 'title':
                this.currentResults.sort((a, b) => a.title.localeCompare(b.title));
                break;
            case 'community':
                this.currentResults.sort((a, b) => {
                    const nameA = this.communities[a.dcwf_community]?.name || '';
                    const nameB = this.communities[b.dcwf_community]?.name || '';
                    return nameA.localeCompare(nameB);
                });
                break;
            case 'category':
                this.currentResults.sort((a, b) => {
                    const nameA = this.categories[a.ncwf_category]?.name || '';
                    const nameB = this.categories[b.ncwf_category]?.name || '';
                    return nameA.localeCompare(nameB);
                });
                break;
            case 'relevance':
            default:
                if (this.currentResults[0]?.similarityScore !== undefined) {
                    this.currentResults.sort((a, b) => (b.similarityScore || 0) - (a.similarityScore || 0));
                } else if (this.currentResults[0]?.questionnaireScore !== undefined) {
                    this.currentResults.sort((a, b) => (b.questionnaireScore || 0) - (a.questionnaireScore || 0));
                }
                break;
        }
        this.renderResults();
    }

    // Recommendations Mode
    initializeRecommendations() {
        console.log('Initializing recommendations');
        // Mode déjà prêt
    }

    getRecommendations() {
        const jobDescriptionEl = document.getElementById('job-description');
        const description = jobDescriptionEl.value.trim();
        
        if (!description || description.length < 20) {
            alert('Veuillez fournir une description plus détaillée de votre poste (au moins 20 caractères).');
            return;
        }

        const recommendations = this.calculateRecommendations(description);
        this.currentResults = recommendations.slice(0, 10);
        this.showResults();
    }

    calculateRecommendations(description) {
        const inputWords = this.extractKeywords(description.toLowerCase());
        
        const scoredRoles = this.workRoles.map(role => {
            const score = this.calculateMatchScore(inputWords, role);
            return { ...role, similarityScore: score };
        });

        return scoredRoles
            .filter(role => role.similarityScore > 5)
            .sort((a, b) => b.similarityScore - a.similarityScore);
    }

    extractKeywords(text) {
        const stopWords = new Set([
            'le', 'la', 'les', 'de', 'du', 'des', 'et', 'ou', 'un', 'une', 'dans', 'sur', 'avec', 'pour', 'par',
            'ce', 'qui', 'que', 'est', 'sont', 'avoir', 'être', 'the', 'and', 'or', 'of', 'to', 'in', 'on', 'at',
            'for', 'with', 'by', 'as', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had'
        ]);

        return text
            .replace(/[.,;:!?()"-]/g, ' ')
            .split(/\s+/)
            .map(word => word.trim())
            .filter(word => word.length > 2 && !stopWords.has(word))
            .filter(word => !/^\d+$/.test(word));
    }

    calculateMatchScore(inputWords, role) {
        let score = 0;
        const roleKeywords = role.keywords.map(k => k.toLowerCase());
        const roleTitle = role.title.toLowerCase();
        const roleDescription = role.description.toLowerCase();

        inputWords.forEach(word => {
            if (roleKeywords.includes(word)) {
                score += 5;
            } else if (roleTitle.includes(word)) {
                score += 3;
            } else if (roleDescription.includes(word)) {
                score += 2;
            } else if (roleKeywords.some(k => k.includes(word) || word.includes(k))) {
                score += 1;
            }
        });

        const matchingKeywords = roleKeywords.filter(k => 
            inputWords.some(word => k.includes(word) || word.includes(k))
        );
        if (matchingKeywords.length > 2) {
            score += matchingKeywords.length * 2;
        }

        return Math.min(100, Math.round((score / Math.max(inputWords.length, 1)) * 10));
    }

    // Results Display
    showResults() {
        console.log(`Showing ${this.currentResults.length} results`);
        const resultsSection = document.getElementById('results-section');
        if (resultsSection) {
            resultsSection.style.display = 'block';
        }
        this.renderResults();
        
        setTimeout(() => {
            if (resultsSection) {
                resultsSection.scrollIntoView({ 
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }, 100);
    }

    renderResults() {
        const container = document.getElementById('results-grid');
        const emptyResults = document.getElementById('empty-results');
        const counter = document.getElementById('results-count');

        if (counter) counter.textContent = this.currentResults.length;

        if (this.currentResults.length === 0) {
            if (container) container.style.display = 'none';
            if (emptyResults) emptyResults.style.display = 'block';
            return;
        }

        if (container) container.style.display = 'grid';
        if (emptyResults) emptyResults.style.display = 'none';
        if (container) container.innerHTML = '';

        this.currentResults.forEach(role => {
            const card = this.createWorkRoleCard(role);
            if (container) container.appendChild(card);
        });
    }

    createWorkRoleCard(role) {
        const card = document.createElement('div');
        card.className = 'work-role-card';
        
        const communityName = this.communities[role.dcwf_community]?.name || 'Inconnue';
        const categoryName = this.categories[role.ncwf_category]?.name || 'Inconnue';
        
        const similarityScore = role.similarityScore ? 
            `<div class="similarity-score">${Math.round(role.similarityScore)}%</div>` : 
            (role.questionnaireScore ? `<div class="similarity-score">${Math.round(role.questionnaireScore * 10)}%</div>` : '');

        card.innerHTML = `
            <div class="work-role-header">
                <div class="work-role-ids">
                    <span class="work-role-id">OMP-ID: ${role.omp_id}</span>
                    <span class="work-role-id">WRL-ID: ${role.wrl_id}</span>
                </div>
                <h4 class="work-role-title">${role.title}</h4>
            </div>
            <p class="work-role-description">${role.description}</p>
            <div class="work-role-badges">
                <span class="work-role-badge work-role-badge--community">${communityName}</span>
                <span class="work-role-badge work-role-badge--category">${categoryName}</span>
                <span class="work-role-badge work-role-badge--ncwf-2025">NCWF 2025</span>
                <span class="work-role-badge work-role-badge--dcwf-2025">DCWF 2025</span>
            </div>
            <div class="work-role-keywords">
                ${role.keywords.slice(0, 8).map(keyword => 
                    `<span class="keyword-tag">${keyword}</span>`
                ).join('')}
                ${role.keywords.length > 8 ? '<span class="keyword-tag">...</span>' : ''}
            </div>
            ${similarityScore}
        `;

        card.addEventListener('click', () => {
            this.showWorkRoleModal(role);
        });

        return card;
    }

    // Modal
    showWorkRoleModal(role) {
        const modal = document.getElementById('work-role-modal');
        const title = document.getElementById('modal-title');
        const body = document.getElementById('modal-body');

        if (title) title.textContent = role.title;

        const communityInfo = this.communities[role.dcwf_community];
        const categoryInfo = this.categories[role.ncwf_category];

        if (body) {
            body.innerHTML = `
                <div class="modal-section">
                    <h4>Identifiants</h4>
                    <p><strong>OMP-ID:</strong> ${role.omp_id}</p>
                    <p><strong>WRL-ID:</strong> ${role.wrl_id}</p>
                </div>
                
                <div class="modal-section">
                    <h4>Description complète</h4>
                    <p>${role.description}</p>
                </div>
                
                <div class="modal-section">
                    <h4>Communauté DCWF</h4>
                    <p class="text-primary"><strong>${communityInfo?.name || 'Inconnue'}</strong></p>
                    <p>${communityInfo?.description || 'Description non disponible'}</p>
                </div>
                
                <div class="modal-section">
                    <h4>Catégorie NCWF</h4>
                    <p class="text-primary"><strong>${categoryInfo?.name || 'Inconnue'}</strong></p>
                    <p>${categoryInfo?.description || 'Description non disponible'}</p>
                </div>
                
                <div class="modal-section">
                    <h4>Mots-clés associés</h4>
                    <div class="work-role-keywords">
                        ${role.keywords.map(keyword => 
                            `<span class="keyword-tag">${keyword}</span>`
                        ).join('')}
                    </div>
                </div>
                
                ${role.similarityScore ? `
                    <div class="modal-section">
                        <h4>Score de compatibilité</h4>
                        <p>Ce rôle correspond à <strong>${Math.round(role.similarityScore)}%</strong> à votre description.</p>
                    </div>
                ` : ''}
                
                ${role.questionnaireScore ? `
                    <div class="modal-section">
                        <h4>Score questionnaire</h4>
                        <p>Ce rôle correspond à <strong>${Math.round(role.questionnaireScore * 10)}%</strong> à vos réponses.</p>
                    </div>
                ` : ''}
            `;
        }

        const backdrop = modal.querySelector('.modal-backdrop');
        if (backdrop) {
            const newBackdrop = backdrop.cloneNode(true);
            backdrop.parentNode.replaceChild(newBackdrop, backdrop);
            
            newBackdrop.addEventListener('click', () => {
                this.closeModal();
            });
        }

        if (modal) modal.classList.remove('hidden');
    }

    closeModal() {
        const modal = document.getElementById('work-role-modal');
        if (modal) {
            modal.classList.add('hidden');
        }
    }

    // Export
    exportResults() {
        if (this.currentResults.length === 0) {
            alert('Aucun résultat à exporter.');
            return;
        }

        const csvContent = this.generateCSV();
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        
        const link = document.createElement('a');
        link.href = url;
        link.download = `dcwf_work_roles_${new Date().toISOString().split('T')[0]}.csv`;
        link.style.display = 'none';
        
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        
        URL.revokeObjectURL(url);
    }

    generateCSV() {
        const headers = [
            'OMP-ID',
            'WRL-ID',
            'Titre',
            'Description',
            'Communauté DCWF',
            'Catégorie NCWF',
            'Mots-clés',
            'Score de compatibilité'
        ];

        const rows = this.currentResults.map(role => [
            role.omp_id,
            role.wrl_id,
            `"${role.title.replace(/"/g, '""')}"`,
            `"${role.description.replace(/"/g, '""')}"`,
            this.communities[role.dcwf_community]?.name || '',
            this.categories[role.ncwf_category]?.name || '',
            `"${role.keywords.join('; ')}"`,
            role.similarityScore ? `${Math.round(role.similarityScore)}%` : 
            (role.questionnaireScore ? `${Math.round(role.questionnaireScore * 10)}%` : '')
        ]);

        return [headers.join(','), ...rows.map(row => row.join(','))].join('\n');
    }

    // Utilities
    updateStats() {
        const totalRoles = this.workRoles.length;
        const totalRolesEl = document.getElementById('total-roles-counter');
        if (totalRolesEl) {
            totalRolesEl.textContent = totalRoles;
        }
    }

    showLoading() {
        const loadingOverlay = document.getElementById('loading-overlay');
        if (loadingOverlay) {
            loadingOverlay.classList.remove('hidden');
        }
    }

    hideLoading() {
        const loadingOverlay = document.getElementById('loading-overlay');
        if (loadingOverlay) {
            loadingOverlay.classList.add('hidden');
        }
    }
}

// Initialisation de l'application
document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM loaded, initializing DCWF application...');
    window.dcwfApp = new DCWFApp();
});