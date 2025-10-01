// Application Data
const competenciesData = {
  "competencies": [
    {
      "id": "NF-COM-001",
      "name": "Access Controls",
      "description": "This Competency Area describes a learner's capabilities to define, manage, and monitor the roles and secure access privileges of who is authorized to access protected data and resources and understand the impact of different types of access controls.",
      "category": "Technical",
      "officialStatus": "official",
      "tksAvailability": "K-,S-statements not available",
      "tksStatus": "unavailable",
      "keyFocusAreas": [
        "Role-based access control (RBAC) implementation",
        "Access privilege management and monitoring", 
        "Identity and authentication systems",
        "Access control policy development"
      ],
      "realWorldApplications": [
        "Implementing secure login systems for enterprise applications",
        "Managing user permissions in cloud environments",
        "Designing access control policies for sensitive data"
      ],
      "relatedSkills": [
        "Knowledge of authentication protocols",
        "Skill in configuring access control systems",
        "Knowledge of identity management frameworks",
        "Skill in access audit procedures"
      ],
      "careerRelevance": [
        "Identity and Access Management Specialist",
        "Security Administrator",
        "Systems Security Analyst",
        "Cloud Security Engineer"
      ],
      "buildingBlocks": [
        "Task: Configure role-based access controls",
        "Knowledge: Understanding of authentication methods",
        "Skill: Ability to implement multi-factor authentication"
      ]
    },
    {
      "id": "NF-COM-002", 
      "name": "Artificial Intelligence (AI) Security",
      "description": "This Competency Area describes a learner's capabilities to secure Artificial Intelligence (AI) against cyberattacks, to ensure it is adequately contained where it is used, and to mitigate the threat AI presents where it or its users have malicious intent",
      "category": "Emerging Technology",
      "officialStatus": "official",
      "tksAvailability": "K-,S-statements available (39 K-statements, 7 S-statements)",
      "tksStatus": "available",
      "keyFocusAreas": [
        "AI model security and protection",
        "Machine learning threat detection",
        "AI system containment and isolation",
        "Malicious AI threat mitigation"
      ],
      "realWorldApplications": [
        "Securing AI models from adversarial attacks",
        "Implementing AI-powered security monitoring systems",
        "Protecting against deepfake and AI-generated threats"
      ],
      "relatedSkills": [
        "Knowledge of machine learning algorithms",
        "Skill in AI model validation",
        "Knowledge of adversarial machine learning",
        "Skill in AI threat assessment"
      ],
      "careerRelevance": [
        "AI Security Specialist",
        "Machine Learning Security Engineer",
        "AI Risk Assessment Analyst",
        "Emerging Technology Security Consultant"
      ],
      "buildingBlocks": [
        "Task: Assess AI system vulnerabilities",
        "Knowledge: Understanding of neural network security",
        "Skill: Ability to implement AI model protection"
      ]
    },
    {
      "id": "NF-COM-003",
      "name": "Asset Management", 
      "description": "This Competency Area describes a learner's capabilities to conduct and maintain an accurate inventory of all digital assets, to include identifying, developing, operating, maintaining, upgrading, and disposing of assets.",
      "category": "Technical",
      "officialStatus": "official",
      "tksAvailability": "K-,S-statements not available",
      "tksStatus": "unavailable",
      "keyFocusAreas": [
        "Digital asset inventory management",
        "Asset lifecycle management",
        "Asset classification and tagging",
        "Asset disposal and decommissioning"
      ],
      "realWorldApplications": [
        "Maintaining comprehensive IT asset databases",
        "Implementing automated asset discovery tools",
        "Managing software license compliance"
      ],
      "relatedSkills": [
        "Knowledge of asset management tools",
        "Skill in asset inventory procedures",
        "Knowledge of asset classification schemes",
        "Skill in asset tracking systems"
      ],
      "careerRelevance": [
        "IT Asset Manager",
        "Configuration Management Analyst",
        "Security Asset Coordinator",
        "IT Infrastructure Specialist"
      ],
      "buildingBlocks": [
        "Task: Maintain digital asset inventory",
        "Knowledge: Understanding of asset lifecycle",
        "Skill: Ability to implement asset tracking systems"
      ]
    },
    {
      "id": "NF-COM-004",
      "name": "Cloud Security",
      "description": "This Competency Area describes a learner's capabilities to protect cloud data, applications, and infrastructure from internal and external threats.",
      "category": "Technical", 
      "officialStatus": "official",
      "tksAvailability": "K-,S-statements not available",
      "tksStatus": "unavailable",
      "keyFocusAreas": [
        "Cloud infrastructure security",
        "Cloud data protection and encryption",
        "Multi-cloud security management",
        "Cloud compliance and governance"
      ],
      "realWorldApplications": [
        "Securing AWS, Azure, and GCP environments",
        "Implementing cloud security posture management",
        "Managing hybrid cloud security architectures"
      ],
      "relatedSkills": [
        "Knowledge of cloud security frameworks",
        "Skill in cloud configuration management",
        "Knowledge of container security",
        "Skill in cloud monitoring and logging"
      ],
      "careerRelevance": [
        "Cloud Security Engineer",
        "Cloud Security Architect", 
        "DevSecOps Engineer",
        "Cloud Compliance Manager"
      ],
      "buildingBlocks": [
        "Task: Configure cloud security controls",
        "Knowledge: Understanding of cloud threat models",
        "Skill: Ability to implement cloud encryption"
      ]
    },
    {
      "id": "NF-COM-005",
      "name": "Communications Security",
      "description": "This Competency Area describes a learner's capabilities to secure the transmissions, broadcasting, switching, control, and operation of communications and related network infrastructures.",
      "category": "Technical",
      "officialStatus": "official",
      "tksAvailability": "K-,S-statements not available",
      "tksStatus": "unavailable",
      "keyFocusAreas": [
        "Network communications encryption",
        "Secure communication protocols",
        "Network infrastructure protection",
        "Communication system monitoring"
      ],
      "realWorldApplications": [
        "Implementing secure VPN solutions",
        "Managing encrypted communication channels",
        "Securing wireless communication networks"
      ],
      "relatedSkills": [
        "Knowledge of cryptographic protocols",
        "Skill in network security configuration",
        "Knowledge of communication standards",
        "Skill in network traffic analysis"
      ],
      "careerRelevance": [
        "Network Security Engineer",
        "Communications Security Analyst",
        "Network Infrastructure Specialist",
        "Telecommunications Security Manager"
      ],
      "buildingBlocks": [
        "Task: Implement secure communication protocols",
        "Knowledge: Understanding of network encryption",
        "Skill: Ability to configure secure networks"
      ]
    },
    {
      "id": "NF-COM-006",
      "name": "Cryptography",
      "description": "This Competency Area describes a learner's capabilities to transform data using cryptographic processes to ensure it can only be read by the person who is authorized to access it.",
      "category": "Technical",
      "officialStatus": "official",
      "tksAvailability": "K-,S-statements not available",
      "tksStatus": "unavailable",
      "keyFocusAreas": [
        "Encryption algorithm implementation",
        "Key management systems",
        "Digital signatures and certificates",
        "Cryptographic protocol design"
      ],
      "realWorldApplications": [
        "Implementing end-to-end encryption systems",
        "Managing public key infrastructure (PKI)",
        "Designing secure authentication mechanisms"
      ],
      "relatedSkills": [
        "Knowledge of encryption algorithms",
        "Skill in cryptographic implementation",
        "Knowledge of key management practices",
        "Skill in digital certificate management"
      ],
      "careerRelevance": [
        "Cryptographic Engineer",
        "Information Security Analyst",
        "PKI Specialist",
        "Security Software Developer"
      ],
      "buildingBlocks": [
        "Task: Implement encryption systems",
        "Knowledge: Understanding of cryptographic algorithms",
        "Skill: Ability to manage cryptographic keys"
      ]
    },
    {
      "id": "NF-COM-007",
      "name": "Cyber Resiliency",
      "description": "This Competency Area describes a learner's capability related to architecting, designing, developing, implementing, and maintaining the trustworthiness of systems that use or are enabled by cyber resources in order to anticipate, withstand, recover from, and adapt to adverse conditions, stresses, attacks, or compromises.",
      "category": "Strategic",
      "officialStatus": "official",
      "tksAvailability": "K-,S-statements available",
      "tksStatus": "available",
      "keyFocusAreas": [
        "Resilient system architecture design",
        "Business continuity planning",
        "Disaster recovery implementation",
        "Adaptive security measures"
      ],
      "realWorldApplications": [
        "Designing fault-tolerant cybersecurity systems",
        "Implementing business continuity strategies",
        "Creating incident response and recovery plans"
      ],
      "relatedSkills": [
        "Knowledge of resilience frameworks",
        "Skill in continuity planning",
        "Knowledge of recovery procedures",
        "Skill in risk assessment"
      ],
      "careerRelevance": [
        "Business Continuity Manager",
        "Cyber Resilience Architect",
        "Risk Management Specialist",
        "Security Operations Manager"
      ],
      "buildingBlocks": [
        "Task: Design resilient security architectures",
        "Knowledge: Understanding of continuity principles",
        "Skill: Ability to implement recovery procedures"
      ]
    },
    {
      "id": "NF-COM-008",
      "name": "DevSecOps",
      "description": "This Competency Area describes a learner's capabilities to integrate security as a shared responsibility throughout the development, security, and operations (DevSecOps) life cycle of technologies.",
      "category": "Technical",
      "officialStatus": "official",
      "tksAvailability": "K-,S-statements not available",
      "tksStatus": "unavailable",
      "keyFocusAreas": [
        "Security integration in development pipelines",
        "Automated security testing",
        "Infrastructure as code security",
        "Continuous security monitoring"
      ],
      "realWorldApplications": [
        "Implementing security in CI/CD pipelines", 
        "Automating vulnerability scanning in development",
        "Managing secure container deployment"
      ],
      "relatedSkills": [
        "Knowledge of DevOps practices",
        "Skill in automation tools",
        "Knowledge of secure coding practices",
        "Skill in container security"
      ],
      "careerRelevance": [
        "DevSecOps Engineer",
        "Security Automation Specialist",
        "Application Security Engineer",
        "Cloud DevOps Engineer"
      ],
      "buildingBlocks": [
        "Task: Integrate security into development workflows",
        "Knowledge: Understanding of DevOps security practices",
        "Skill: Ability to automate security testing"
      ]
    },
    {
      "id": "NF-COM-009",
      "name": "Operating Systems (OS) Security",
      "description": "This Competency Area describes a learner's capabilities to install, administer, troubleshoot, backup, and conduct recovery of Operating Systems (OS), including in simulated environments.",
      "category": "Technical",
      "officialStatus": "official",
      "tksAvailability": "K-,S-statements not available",
      "tksStatus": "unavailable",
      "keyFocusAreas": [
        "OS hardening and configuration",
        "System administration security",
        "OS vulnerability management",
        "System backup and recovery"
      ],
      "realWorldApplications": [
        "Securing Windows and Linux server environments",
        "Implementing OS-level access controls",
        "Managing system patches and updates"
      ],
      "relatedSkills": [
        "Knowledge of OS security features",
        "Skill in system hardening",
        "Knowledge of backup procedures",
        "Skill in OS troubleshooting"
      ],
      "careerRelevance": [
        "Systems Administrator",
        "OS Security Specialist",
        "Infrastructure Security Analyst",
        "System Security Engineer"
      ],
      "buildingBlocks": [
        "Task: Configure secure operating systems",
        "Knowledge: Understanding of OS security mechanisms",
        "Skill: Ability to implement system hardening"
      ]
    },
    {
      "id": "NF-COM-010",
      "name": "Operational Technology (OT) Security",
      "description": "This Competency Area describes a learner's capabilities to improve and maintain the security of Operational Technology (OT) systems while addressing their unique performance, reliability, and safety requirements.",
      "category": "Specialized",
      "officialStatus": "official",
      "tksAvailability": "K-,S-statements not available",
      "tksStatus": "unavailable",
      "keyFocusAreas": [
        "Industrial control system security",
        "SCADA system protection",
        "OT/IT network segmentation", 
        "Critical infrastructure protection"
      ],
      "realWorldApplications": [
        "Securing manufacturing control systems",
        "Protecting power grid infrastructure",
        "Implementing safety-critical system security"
      ],
      "relatedSkills": [
        "Knowledge of industrial protocols",
        "Skill in OT security assessment",
        "Knowledge of safety systems",
        "Skill in network segmentation"
      ],
      "careerRelevance": [
        "OT Security Specialist",
        "Industrial Control Systems Engineer",
        "Critical Infrastructure Analyst",
        "SCADA Security Engineer"
      ],
      "buildingBlocks": [
        "Task: Secure operational technology systems",
        "Knowledge: Understanding of industrial control systems",
        "Skill: Ability to implement OT security controls"
      ]
    },
    {
      "id": "NF-COM-011",
      "name": "Supply Chain Security",
      "description": "This Competency Area describes a learner's capabilities to analyze and control digital and physical risks presented by technology products or services purchased from parties outside your organization.",
      "category": "Strategic",
      "officialStatus": "official",
      "tksAvailability": "K-,S-statements not available",
      "tksStatus": "unavailable",
      "keyFocusAreas": [
        "Vendor risk assessment",
        "Third-party security evaluation",
        "Supply chain threat analysis",
        "Procurement security controls"
      ],
      "realWorldApplications": [
        "Assessing software vendor security practices",
        "Managing hardware supply chain risks",
        "Implementing third-party risk management programs"
      ],
      "relatedSkills": [
        "Knowledge of supply chain risks",
        "Skill in vendor assessment",
        "Knowledge of procurement security",
        "Skill in risk analysis"
      ],
      "careerRelevance": [
        "Supply Chain Risk Analyst",
        "Vendor Risk Manager",
        "Third-Party Risk Specialist",
        "Procurement Security Analyst"
      ],
      "buildingBlocks": [
        "Task: Assess supply chain security risks",
        "Knowledge: Understanding of vendor risk models",
        "Skill: Ability to evaluate third-party security"
      ]
    },
    {
      "id": "NF-COM-012",
      "name": "Cybersecurity Fundamentals",
      "description": "This Competency Area describes a learner's capabilities to understand and apply core cybersecurity principles including the CIA triad (confidentiality, integrity, availability), identify common threat vectors and attack surfaces, comprehend fundamental risk management concepts, and demonstrate knowledge of essential cybersecurity terminology, frameworks, and best practices that form the foundation for all cybersecurity disciplines.",
      "category": "Foundational",
      "officialStatus": "unofficial",
      "tksAvailability": "These Competency Areas have not been officially published",
      "tksStatus": "unofficial",
      "keyFocusAreas": [
        "CIA triad principles application",
        "Threat landscape understanding",
        "Risk management fundamentals",
        "Security frameworks knowledge"
      ],
      "realWorldApplications": [
        "Conducting basic risk assessments",
        "Implementing fundamental security controls",
        "Understanding organizational security posture"
      ],
      "relatedSkills": [
        "Knowledge of security principles",
        "Skill in risk identification",
        "Knowledge of security frameworks",
        "Skill in basic threat analysis"
      ],
      "careerRelevance": [
        "Entry-level Security Analyst",
        "Cybersecurity Trainee",
        "Security Awareness Coordinator",
        "IT Security Intern"
      ],
      "buildingBlocks": [
        "Task: Apply basic security principles",
        "Knowledge: Understanding of CIA triad",
        "Skill: Ability to identify common threats"
      ]
    },
    {
      "id": "NF-COM-013",
      "name": "Cybersecurity Leadership",
      "description": "This Competency Area describes a learner's capabilities to lead cybersecurity initiatives and teams through strategic planning, effective communication of security concepts to diverse stakeholders, development of security culture within organizations, risk prioritization and resource allocation, incident response coordination, and the ability to align cybersecurity objectives with business goals while fostering collaboration across organizational boundaries.",
      "category": "Management",
      "officialStatus": "unofficial",
      "tksAvailability": "These Competency Areas have not been officially published",
      "tksStatus": "unofficial",
      "keyFocusAreas": [
        "Strategic cybersecurity planning",
        "Security team leadership",
        "Stakeholder communication",
        "Security culture development"
      ],
      "realWorldApplications": [
        "Leading enterprise security programs",
        "Managing cybersecurity budgets and resources",
        "Coordinating incident response teams"
      ],
      "relatedSkills": [
        "Knowledge of leadership principles",
        "Skill in strategic planning",
        "Knowledge of communication strategies",
        "Skill in team management"
      ],
      "careerRelevance": [
        "Chief Information Security Officer (CISO)",
        "Security Program Manager",
        "Cybersecurity Director",
        "Security Team Lead"
      ],
      "buildingBlocks": [
        "Task: Develop security strategies",
        "Knowledge: Understanding of leadership frameworks",
        "Skill: Ability to manage security teams"
      ]
    },
    {
      "id": "NF-COM-014",
      "name": "Data Security",
      "description": "This Competency Area describes a learner's capabilities to protect digital information throughout its entire lifecycle from creation to destruction, implement data classification schemes and access controls, apply appropriate encryption and data masking techniques, ensure compliance with data protection regulations, and maintain data integrity and availability while preventing unauthorized access, corruption, or theft of sensitive information.",
      "category": "Technical",
      "officialStatus": "unofficial",
      "tksAvailability": "These Competency Areas have not been officially published",
      "tksStatus": "unofficial",
      "keyFocusAreas": [
        "Data lifecycle protection",
        "Data classification and labeling",
        "Encryption and data masking",
        "Data privacy compliance"
      ],
      "realWorldApplications": [
        "Implementing data loss prevention systems",
        "Managing GDPR and privacy compliance",
        "Securing databases and data warehouses"
      ],
      "relatedSkills": [
        "Knowledge of data protection methods",
        "Skill in data classification",
        "Knowledge of privacy regulations",
        "Skill in encryption implementation"
      ],
      "careerRelevance": [
        "Data Protection Officer",
        "Database Security Administrator",
        "Privacy Compliance Analyst",
        "Information Security Analyst"
      ],
      "buildingBlocks": [
        "Task: Implement data protection controls",
        "Knowledge: Understanding of data lifecycle",
        "Skill: Ability to classify sensitive data"
      ]
    },
    {
      "id": "NF-COM-015",
      "name": "Secure Programming",
      "description": "This Competency Area describes a learner's capabilities to develop computer software using secure coding practices that prevent the introduction of security vulnerabilities, identify and remediate common programming flaws, implement security controls within application architecture, conduct code security reviews, and integrate security considerations throughout the software development lifecycle to protect against both known and emerging threats.",
      "category": "Technical",
      "officialStatus": "unofficial",
      "tksAvailability": "These Competency Areas have not been officially published",
      "tksStatus": "unofficial",
      "keyFocusAreas": [
        "Secure coding practices",
        "Vulnerability identification and remediation",
        "Application security architecture",
        "Code security reviews"
      ],
      "realWorldApplications": [
        "Developing secure web applications",
        "Implementing input validation and sanitization",
        "Conducting security code reviews"
      ],
      "relatedSkills": [
        "Knowledge of secure coding standards",
        "Skill in vulnerability assessment",
        "Knowledge of application security",
        "Skill in code review techniques"
      ],
      "careerRelevance": [
        "Application Security Engineer",
        "Secure Software Developer",
        "Security Code Reviewer",
        "Software Security Architect"
      ],
      "buildingBlocks": [
        "Task: Implement secure coding practices",
        "Knowledge: Understanding of common vulnerabilities",
        "Skill: Ability to conduct security code reviews"
      ]
    }
  ],
  "categories": [
    {"name": "Foundational", "color": "#3B82F6", "description": "Core cybersecurity concepts and principles"},
    {"name": "Technical", "color": "#10B981", "description": "Technical implementation and operational skills"},
    {"name": "Management", "color": "#8B5CF6", "description": "Leadership and strategic management capabilities"},
    {"name": "Strategic", "color": "#F59E0B", "description": "High-level planning and risk management"},
    {"name": "Specialized", "color": "#EF4444", "description": "Niche and domain-specific expertise"},
    {"name": "Emerging Technology", "color": "#EC4899", "description": "Cutting-edge technology security"}
  ]
};

// Application State
let currentView = 'grid';
let filteredCompetencies = [...competenciesData.competencies];
let userProgress = {};
let bookmarkedCompetencies = [];

// Utility Functions
function getCategoryClass(category) {
  return 'category--' + category.toLowerCase().replace(/\s+/g, '-').replace(/[()]/g, '');
}

function getAvailabilityClass(competency) {
  if (competency.officialStatus === 'unofficial') {
    return 'competency-card__availability--unofficial';
  } else if (competency.tksAvailability.includes('available') && !competency.tksAvailability.includes('not available')) {
    return 'competency-card__availability--available';
  } else {
    return 'competency-card__availability--unavailable';
  }
}

// Initialize Application
function init() {
  populateCategoryFilter();
  renderCompetencies();
  bindEventListeners();
  updateViewButtons();
}

function populateCategoryFilter() {
  const categoryFilter = document.getElementById('categoryFilter');
  if (!categoryFilter) return;
  
  categoryFilter.innerHTML = '<option value="">All Categories</option>';
  
  competenciesData.categories.forEach(category => {
    const option = document.createElement('option');
    option.value = category.name;
    option.textContent = category.name;
    categoryFilter.appendChild(option);
  });
}

// Event Listeners
function bindEventListeners() {
  // Search functionality
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.addEventListener('input', applyFilters);
  }
  
  // Filter functionality
  const categoryFilter = document.getElementById('categoryFilter');
  if (categoryFilter) {
    categoryFilter.addEventListener('change', applyFilters);
  }
  
  const sortSelect = document.getElementById('sortSelect');
  if (sortSelect) {
    sortSelect.addEventListener('change', applyFilters);
  }
  
  const progressFilter = document.getElementById('progressFilter');
  if (progressFilter) {
    progressFilter.addEventListener('change', applyFilters);
  }
  
  const clearFilters = document.getElementById('clearFilters');
  if (clearFilters) {
    clearFilters.addEventListener('click', clearAllFilters);
  }
  
  // View toggle
  const gridViewBtn = document.getElementById('gridView');
  const listViewBtn = document.getElementById('listView');
  
  if (gridViewBtn) {
    gridViewBtn.addEventListener('click', () => setView('grid'));
  }
  
  if (listViewBtn) {
    listViewBtn.addEventListener('click', () => setView('list'));
  }
  
  // Modal functionality
  const modalClose = document.getElementById('modalClose');
  const modalBackdrop = document.getElementById('modalBackdrop');
  
  if (modalClose) {
    modalClose.addEventListener('click', closeModal);
  }
  
  if (modalBackdrop) {
    modalBackdrop.addEventListener('click', closeModal);
  }
  
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeModal();
  });
  
  // Navigation functionality
  const navLinks = document.querySelectorAll('.nav__link');
  navLinks.forEach(link => {
    link.addEventListener('click', handleNavigation);
  });
  
  // Mobile menu toggle
  const menuToggle = document.getElementById('menuToggle');
  if (menuToggle) {
    menuToggle.addEventListener('click', toggleMobileMenu);
  }
}

// Search and Filter Functions
function applyFilters() {
  const searchInput = document.getElementById('searchInput');
  const categoryFilter = document.getElementById('categoryFilter');
  const progressFilter = document.getElementById('progressFilter');
  const sortSelect = document.getElementById('sortSelect');
  
  const searchTerm = searchInput ? searchInput.value.toLowerCase() : '';
  const categoryValue = categoryFilter ? categoryFilter.value : '';
  const progressValue = progressFilter ? progressFilter.value : '';
  const sortBy = sortSelect ? sortSelect.value : 'id';
  
  // Filter competencies
  filteredCompetencies = competenciesData.competencies.filter(competency => {
    const matchesSearch = searchTerm === '' || 
      competency.name.toLowerCase().includes(searchTerm) ||
      competency.description.toLowerCase().includes(searchTerm) ||
      competency.keyFocusAreas.some(area => area.toLowerCase().includes(searchTerm));
    
    const matchesCategory = categoryValue === '' || competency.category === categoryValue;
    
    const progress = userProgress[competency.id] || 'unset';
    const matchesProgress = progressValue === '' || 
      (progressValue === 'unset' && progress === 'unset') ||
      progress === progressValue;
    
    return matchesSearch && matchesCategory && matchesProgress;
  });
  
  // Sort competencies
  filteredCompetencies.sort((a, b) => {
    switch (sortBy) {
      case 'name':
        return a.name.localeCompare(b.name);
      case 'category':
        return a.category.localeCompare(b.category);
      case 'id':
      default:
        return a.id.localeCompare(b.id);
    }
  });
  
  renderCompetencies();
}

function clearAllFilters() {
  const searchInput = document.getElementById('searchInput');
  const categoryFilter = document.getElementById('categoryFilter');
  const progressFilter = document.getElementById('progressFilter');
  const sortSelect = document.getElementById('sortSelect');
  
  if (searchInput) searchInput.value = '';
  if (categoryFilter) categoryFilter.value = '';
  if (progressFilter) progressFilter.value = '';
  if (sortSelect) sortSelect.value = 'id';
  
  applyFilters();
}

// View Functions
function setView(view) {
  currentView = view;
  updateViewButtons();
  updateViewLayout();
  renderCompetencies();
}

function updateViewButtons() {
  const gridViewBtn = document.getElementById('gridView');
  const listViewBtn = document.getElementById('listView');
  
  if (gridViewBtn && listViewBtn) {
    if (currentView === 'grid') {
      gridViewBtn.classList.add('btn--primary');
      gridViewBtn.classList.remove('btn--outline');
      listViewBtn.classList.add('btn--outline');
      listViewBtn.classList.remove('btn--primary');
    } else {
      listViewBtn.classList.add('btn--primary');
      listViewBtn.classList.remove('btn--outline');
      gridViewBtn.classList.add('btn--outline');
      gridViewBtn.classList.remove('btn--primary');
    }
  }
}

function updateViewLayout() {
  const competenciesContainer = document.getElementById('competenciesContainer');
  if (competenciesContainer) {
    if (currentView === 'list') {
      competenciesContainer.classList.add('competencies-grid--list');
    } else {
      competenciesContainer.classList.remove('competencies-grid--list');
    }
  }
}

// Render Functions
function renderCompetencies() {
  const competenciesContainer = document.getElementById('competenciesContainer');
  const noResults = document.getElementById('noResults');
  
  if (!competenciesContainer) return;
  
  competenciesContainer.innerHTML = '';
  
  if (filteredCompetencies.length === 0) {
    if (noResults) {
      noResults.classList.remove('hidden');
    }
    return;
  }
  
  if (noResults) {
    noResults.classList.add('hidden');
  }
  
  filteredCompetencies.forEach(competency => {
    const card = createCompetencyCard(competency);
    competenciesContainer.appendChild(card);
  });
}

function createCompetencyCard(competency) {
  const card = document.createElement('div');
  card.className = `competency-card${currentView === 'list' ? ' competency-card--list' : ''}`;
  card.setAttribute('tabindex', '0');
  card.setAttribute('role', 'button');
  card.setAttribute('aria-label', `View details for ${competency.name}`);
  
  const isBookmarked = bookmarkedCompetencies.includes(competency.id);
  const progress = userProgress[competency.id] || 'unset';
  
  card.innerHTML = `
    <div class="competency-card__header">
      <div class="competency-card__id">${competency.id}</div>
      <h3 class="competency-card__name">${competency.name}</h3>
      <span class="competency-card__category ${getCategoryClass(competency.category)}">${competency.category}</span>
    </div>
    <div class="competency-card__body">
      <p class="competency-card__description">${competency.description}</p>
      <div class="competency-card__availability ${getAvailabilityClass(competency)}">
        <strong>Availability:</strong> ${competency.tksAvailability}
      </div>
    </div>
    <div class="competency-card__footer">
      <div class="competency-card__actions">
        <div class="progress-tracker">
          <button class="progress-btn ${progress === 'learning' ? 'progress-btn--active' : ''}" 
                  data-id="${competency.id}" data-progress="learning" title="Mark as Learning">
            Learning
          </button>
          <button class="progress-btn ${progress === 'familiar' ? 'progress-btn--active' : ''}" 
                  data-id="${competency.id}" data-progress="familiar" title="Mark as Familiar">
            Familiar
          </button>
          <button class="progress-btn ${progress === 'expert' ? 'progress-btn--active' : ''}" 
                  data-id="${competency.id}" data-progress="expert" title="Mark as Expert">
            Expert
          </button>
        </div>
      </div>
      <button class="bookmark-btn ${isBookmarked ? 'bookmark-btn--active' : ''}" 
              data-id="${competency.id}" title="${isBookmarked ? 'Remove bookmark' : 'Add bookmark'}">
        ${isBookmarked ? '★' : '☆'}
      </button>
    </div>
  `;
  
  // Main card click handler
  card.addEventListener('click', (e) => {
    if (!e.target.closest('.progress-btn') && !e.target.closest('.bookmark-btn')) {
      openModal(competency);
    }
  });
  
  card.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      if (!e.target.closest('.progress-btn') && !e.target.closest('.bookmark-btn')) {
        openModal(competency);
      }
    }
  });
  
  // Progress button handlers
  const progressBtns = card.querySelectorAll('.progress-btn');
  progressBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      handleProgressChange(e);
    });
  });
  
  // Bookmark button handler
  const bookmarkBtn = card.querySelector('.bookmark-btn');
  if (bookmarkBtn) {
    bookmarkBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      handleBookmarkToggle(e);
    });
  }
  
  return card;
}

// Progress and Bookmark Functions
function handleProgressChange(e) {
  const competencyId = e.target.dataset.id;
  const newProgress = e.target.dataset.progress;
  
  if (userProgress[competencyId] === newProgress) {
    delete userProgress[competencyId];
  } else {
    userProgress[competencyId] = newProgress;
  }
  
  renderCompetencies();
}

function handleBookmarkToggle(e) {
  const competencyId = e.target.dataset.id;
  
  if (bookmarkedCompetencies.includes(competencyId)) {
    bookmarkedCompetencies = bookmarkedCompetencies.filter(id => id !== competencyId);
  } else {
    bookmarkedCompetencies.push(competencyId);
  }
  
  renderCompetencies();
}

// Modal Functions
function openModal(competency) {
  const modal = document.getElementById('competencyModal');
  const modalTitle = document.getElementById('modalTitle');
  const modalBody = document.getElementById('modalBody');
  
  if (modalTitle) {
    modalTitle.textContent = `${competency.id}: ${competency.name}`;
  }
  
  if (modalBody) {
    modalBody.innerHTML = createModalContent(competency);
  }
  
  if (modal) {
    modal.classList.remove('hidden');
    modal.setAttribute('aria-hidden', 'false');
  }
  
  const modalClose = document.getElementById('modalClose');
  if (modalClose) {
    modalClose.focus();
  }
}

function closeModal() {
  const modal = document.getElementById('competencyModal');
  if (modal) {
    modal.classList.add('hidden');
    modal.setAttribute('aria-hidden', 'true');
  }
}

function createModalContent(competency) {
  const progressText = userProgress[competency.id] ? 
    userProgress[competency.id].charAt(0).toUpperCase() + userProgress[competency.id].slice(1) : 
    'Not Set';
  
  const statusText = competency.officialStatus === 'official' ? 'Official' : 'Unofficial (Proposed)';
  
  return `
    <div class="modal__meta">
      <div class="modal__meta-item">
        <h4>ID</h4>
        <div class="value">${competency.id}</div>
      </div>
      <div class="modal__meta-item">
        <h4>Category</h4>
        <div class="value">${competency.category}</div>
      </div>
      <div class="modal__meta-item">
        <h4>Status</h4>
        <div class="value">${statusText}</div>
      </div>
      <div class="modal__meta-item">
        <h4>Your Progress</h4>
        <div class="value">${progressText}</div>
      </div>
      <div class="modal__meta-item">
        <h4>TKS Availability</h4>
        <div class="value">${competency.tksAvailability}</div>
      </div>
      <div class="modal__meta-item">
        <h4>Bookmarked</h4>
        <div class="value">${bookmarkedCompetencies.includes(competency.id) ? 'Yes' : 'No'}</div>
      </div>
    </div>
    
    <div class="modal__section">
      <h3>Description</h3>
      <p>${competency.description}</p>
    </div>
    
    <div class="modal__section">
      <h3>Key Focus Areas</h3>
      <ul>
        ${competency.keyFocusAreas.map(area => `<li>${area}</li>`).join('')}
      </ul>
    </div>
    
    <div class="modal__section">
      <h3>Real-World Applications</h3>
      <ul>
        ${competency.realWorldApplications.map(app => `<li>${app}</li>`).join('')}
      </ul>
    </div>
    
    <div class="modal__section">
      <h3>Related Skills</h3>
      <ul>
        ${competency.relatedSkills.map(skill => `<li>${skill}</li>`).join('')}
      </ul>
    </div>
    
    <div class="modal__section">
      <h3>Career Relevance</h3>
      <ul>
        ${competency.careerRelevance.map(career => `<li>${career}</li>`).join('')}
      </ul>
    </div>
    
    <div class="modal__section">
      <h3>Building Blocks (TKS Examples)</h3>
      <ul>
        ${competency.buildingBlocks.map(block => `<li>${block}</li>`).join('')}
      </ul>
    </div>
  `;
}

// Navigation Functions
function handleNavigation(e) {
  e.preventDefault();
  
  const href = e.target.getAttribute('href');
  if (!href || !href.startsWith('#')) return;
  
  const targetSectionId = href.substring(1);
  
  // Update active nav link
  document.querySelectorAll('.nav__link').forEach(link => {
    link.classList.remove('nav__link--active');
  });
  e.target.classList.add('nav__link--active');
  
  // Hide all sections
  document.querySelectorAll('.section').forEach(section => {
    section.classList.remove('section--active');
  });
  
  // Show target section
  const targetSection = document.getElementById(targetSectionId);
  if (targetSection) {
    targetSection.classList.add('section--active');
  }
  
  // Close mobile menu
  const navLinks = document.getElementById('navLinks');
  if (navLinks) {
    navLinks.classList.remove('nav__links--active');
  }
}

function toggleMobileMenu() {
  const navLinks = document.getElementById('navLinks');
  if (navLinks) {
    navLinks.classList.toggle('nav__links--active');
  }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', init);