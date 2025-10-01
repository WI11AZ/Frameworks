// NCWF Work Role Visualization Application

// Application data
const appData = {
  "work_roles": [
    {
      "id": "OG-WRL-001",
      "name": "Communications Security (COMSEC) Management",
      "omp": ["723"],
      "category": "OG",
      "dcwf_info": {
        "opm_id": "723",
        "dcwf_title": "Communications Security (COMSEC) Management",
        "dcwf_description": "Responsible for managing the Communications Security (COMSEC) resources of an organization."
      },
      "tks_related": [
        {"id": "OG-WRL-015", "name": "Technology Portfolio Management", "percentage": 37.5},
        {"id": "OG-WRL-006", "name": "Information Systems/Cybersecurity Management", "percentage": 35.59},
        {"id": "OG-WRL-014", "name": "Systems Security Management", "percentage": 31.86},
        {"id": "IO-WRL-003", "name": "Knowledge Management", "percentage": 31.67},
        {"id": "OG-WRL-016", "name": "Technology Program Auditing", "percentage": 31.25}
      ],
      "on_ramps": [
        {"id": "OG-WRL-014", "name": "Systems Security Management", "percentage": 85.2}
      ],
      "off_ramps": [
        {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development", "percentage": 78.5},
        {"id": "OG-WRL-005", "name": "Cybersecurity Instruction", "percentage": 72.3},
        {"id": "OG-WRL-011", "name": "Secure Project Management", "percentage": 68.9},
        {"id": "OG-WRL-014", "name": "Systems Security Management", "percentage": 65.4}
      ],
      "secondary_roles": [
        {"id": "OG-WRL-014", "name": "Systems Security Management", "percentage": "12.9"},
        {"id": "IO-WRL-005", "name": "Systems Administration", "percentage": "12.1"},
        {"id": "IO-WRL-007", "name": "Technical Support", "percentage": "12.1"},
        {"id": "OG-WRL-001", "name": "Communications Security (COMSEC) Management", "percentage": "5.65"},
        {"id": "OG-WRL-011", "name": "Secure Project Management", "percentage": "5.24"}
      ]
    },
    {
      "id": "OG-WRL-002",
      "name": "Cybersecurity Policy and Planning",
      "omp": ["752"],
      "category": "OG",
      "dcwf_info": {
        "opm_id": "752",
        "dcwf_title": "Cybersecurity Policy and Planning",
        "dcwf_description": "Responsible for developing and maintaining cybersecurity plans, strategy, and policy to support and align with organizational cybersecurity initiatives and regulatory compliance."
      },
      "tks_related": [
        {"id": "OG-WRL-015", "name": "Technology Portfolio Management", "percentage": 54.17},
        {"id": "OG-WRL-003", "name": "Cybersecurity Workforce Management", "percentage": 46.97},
        {"id": "OG-WRL-016", "name": "Technology Program Auditing", "percentage": 37.5},
        {"id": "OG-WRL-006", "name": "Information Systems/Cybersecurity Management", "percentage": 32.2},
        {"id": "OG-WRL-007", "name": "Executive Cybersecurity Leadership", "percentage": 30}
      ],
      "on_ramps": [
        {"id": "OG-WRL-003", "name": "Cybersecurity Workforce Management"},
        {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development"},
        {"id": "OG-WRL-005", "name": "Cybersecurity Instruction"},
        {"id": "OG-WRL-006", "name": "Information Systems/Cybersecurity Management"},
        {"id": "OG-WRL-008", "name": "Privacy Compliance"},
        {"id": "OG-WRL-009", "name": "Product Support Management"},
        {"id": "OG-WRL-010", "name": "Program Management"},
        {"id": "OG-WRL-011", "name": "Secure Project Management"},
        {"id": "OG-WRL-012", "name": "Security Control Assessment"},
        {"id": "OG-WRL-013", "name": "Systems Authorization"},
        {"id": "OG-WRL-014", "name": "Systems Security Management"},
        {"id": "OG-WRL-015", "name": "Technology Portfolio Management"},
        {"id": "OG-WRL-016", "name": "Technology Program Auditing"},
        {"id": "DD-WRL-001", "name": "Cybersecurity Architecture"},
        {"id": "DD-WRL-002", "name": "Enterprise Architecture"},
        {"id": "DD-WRL-003", "name": "Secure Software Development"},
        {"id": "DD-WRL-004", "name": "Secure Systems Development"},
        {"id": "DD-WRL-005", "name": "Software Security Assessment"},
        {"id": "DD-WRL-006", "name": "Systems Requirements Planning"},
        {"id": "DD-WRL-007", "name": "Systems Testing and Evaluation"},
        {"id": "DD-WRL-008", "name": "Technology Research and Development"},
        {"id": "IO-WRL-001", "name": "Data Analysis"},
        {"id": "IO-WRL-002", "name": "Database Administration"},
        {"id": "IO-WRL-003", "name": "Knowledge Management"},
        {"id": "IO-WRL-004", "name": "Network Operations"},
        {"id": "IO-WRL-005", "name": "Systems Administration"},
        {"id": "IO-WRL-006", "name": "Systems Security Analysis"},
        {"id": "IO-WRL-007", "name": "Technical Support"},
        {"id": "PD-WRL-001", "name": "Defensive Cybersecurity"},
        {"id": "PD-WRL-002", "name": "Digital Forensics"},
        {"id": "PD-WRL-003", "name": "Incident Response"},
        {"id": "PD-WRL-004", "name": "Infrastructure Support"},
        {"id": "PD-WRL-007", "name": "Vulnerability Analysis"},
        {"id": "IN-WRL-001", "name": "Cybercrime Investigation"},
        {"id": "IN-WRL-002", "name": "Digital Evidence Analysis"}
      ],
      "off_ramps": [
        {"id": "OG-WRL-013", "name": "Systems Authorization"},
        {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development"},
        {"id": "OG-WRL-005", "name": "Cybersecurity Instruction"},
        {"id": "OG-WRL-008", "name": "Privacy Compliance"},
        {"id": "OG-WRL-003", "name": "Cybersecurity Workforce Management"},
        {"id": "OG-WRL-010", "name": "Program Management"},
        {"id": "OG-WRL-011", "name": "Secure Project Management"},
        {"id": "OG-WRL-007", "name": "Executive Cybersecurity Leadership"}
      ],
      "secondary_roles": [
        {"id": "OG-WRL-010", "name": "Program Management", "percentage": "17.1"},
        {"id": "OG-WRL-011", "name": "Secure Project Management", "percentage": "9.28"},
        {"id": "OG-WRL-003", "name": "Cybersecurity Workforce Management", "percentage": "8.24"},
        {"id": "DD-WRL-006", "name": "Systems Requirements Planning", "percentage": "8.03"},
        {"id": "OG-WRL-014", "name": "Systems Security Management", "percentage": "6.47"}
      ]
    },
    {
      "id": "OG-WRL-003",
      "name": "Cybersecurity Workforce Management",
      "omp": ["751"],
      "category": "OG",
      "tks_related": [
        {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning", "percentage": 91.18},
        {"id": "OG-WRL-015", "name": "Technology Portfolio Management", "percentage": 64.58},
        {"id": "OG-WRL-016", "name": "Technology Program Auditing", "percentage": 45.31},
        {"id": "OG-WRL-007", "name": "Executive Cybersecurity Leadership", "percentage": 43},
        {"id": "OG-WRL-013", "name": "Systems Authorization", "percentage": 38.83}
      ],
      "on_ramps": [
        {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning"},
        {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development"},
        {"id": "OG-WRL-005", "name": "Cybersecurity Instruction"},
        {"id": "OG-WRL-008", "name": "Privacy Compliance"},
        {"id": "OG-WRL-009", "name": "Product Support Management"},
        {"id": "OG-WRL-010", "name": "Program Management"},
        {"id": "OG-WRL-011", "name": "Secure Project Management"},
        {"id": "OG-WRL-012", "name": "Security Control Assessment"},
        {"id": "OG-WRL-014", "name": "Systems Security Management"},
        {"id": "DD-WRL-003", "name": "Secure Software Development"},
        {"id": "DD-WRL-004", "name": "Secure Systems Development"},
        {"id": "DD-WRL-005", "name": "Software Security Assessment"},
        {"id": "DD-WRL-006", "name": "Systems Requirements Planning"},
        {"id": "DD-WRL-007", "name": "Systems Testing and Evaluation"},
        {"id": "DD-WRL-008", "name": "Technology Research and Development"},
        {"id": "IO-WRL-001", "name": "Data Analysis"},
        {"id": "IO-WRL-002", "name": "Database Administration"},
        {"id": "IO-WRL-003", "name": "Knowledge Management"},
        {"id": "IO-WRL-004", "name": "Network Operations"},
        {"id": "IO-WRL-005", "name": "Systems Administration"},
        {"id": "IO-WRL-006", "name": "Systems Security Analysis"},
        {"id": "IO-WRL-007", "name": "Technical Support"},
        {"id": "PD-WRL-001", "name": "Defensive Cybersecurity"},
        {"id": "PD-WRL-002", "name": "Digital Forensics"},
        {"id": "PD-WRL-003", "name": "Incident Response"},
        {"id": "PD-WRL-004", "name": "Infrastructure Support"},
        {"id": "PD-WRL-007", "name": "Vulnerability Analysis"},
        {"id": "IN-WRL-001", "name": "Cybercrime Investigation"},
        {"id": "IN-WRL-002", "name": "Digital Evidence Analysis"}
      ],
      "off_ramps": [
        {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development"},
        {"id": "OG-WRL-005", "name": "Cybersecurity Instruction"},
        {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning"},
        {"id": "OG-WRL-011", "name": "Secure Project Management"}
      ],
      "secondary_roles": [
        {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning", "percentage": "34.51"},
        {"id": "OG-WRL-010", "name": "Program Management", "percentage": "21.77"},
        {"id": "OG-WRL-011", "name": "Secure Project Management", "percentage": "5.84"},
        {"id": "OG-WRL-014", "name": "Systems Security Management", "percentage": "5.84"},
        {"id": "DD-WRL-006", "name": "Systems Requirements Planning", "percentage": "3.89"}
      ]
    },
    {
      "id": "DD-WRL-001",
      "name": "Cybersecurity Architecture",
      "omp": ["652"],
      "category": "DD",
      "tks_related": [
        {"id": "DD-WRL-002", "name": "Enterprise Architecture", "percentage": 90.38},
        {"id": "IO-WRL-006", "name": "Systems Security Analysis", "percentage": 58},
        {"id": "DD-WRL-004", "name": "Secure Systems Development", "percentage": 52.59},
        {"id": "DD-WRL-006", "name": "Systems Requirements Planning", "percentage": 51.45},
        {"id": "IO-WRL-004", "name": "Network Operations", "percentage": 49.18}
      ],
      "on_ramps": [
        {"id": "DD-WRL-002", "name": "Enterprise Architecture"},
        {"id": "DD-WRL-004", "name": "Secure Systems Development"},
        {"id": "DD-WRL-008", "name": "Technology Research and Development"}
      ],
      "off_ramps": [
        {"id": "DD-WRL-002", "name": "Enterprise Architecture"},
        {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development"},
        {"id": "OG-WRL-005", "name": "Cybersecurity Instruction"},
        {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning"},
        {"id": "OG-WRL-010", "name": "Program Management"},
        {"id": "OG-WRL-007", "name": "Executive Cybersecurity Leadership"}
      ],
      "secondary_roles": [
        {"id": "DD-WRL-004", "name": "Secure Systems Development", "percentage": "13.74"},
        {"id": "IO-WRL-006", "name": "Systems Security Analysis", "percentage": "12.8"},
        {"id": "DD-WRL-002", "name": "Enterprise Architecture", "percentage": "8.53"},
        {"id": "DD-WRL-006", "name": "Systems Requirements Planning", "percentage": "8.06"},
        {"id": "OG-WRL-011", "name": "Secure Project Management", "percentage": "5.69"}
      ]
    }
  ],
  "categories": {
    "DD": {"class": "design-development", "name": "Design and Development", "roles": 9},
    "IN": {"class": "investigation", "name": "Investigation", "roles": 2},
    "IO": {"class": "implementation-operation", "name": "Implementation and Operation", "roles": 7},
    "OG": {"class": "oversight-governance", "name": "Oversight and Governance", "roles": 16},
    "PD": {"class": "protection-defense", "name": "Protection and Defense", "roles": 7}
  }
};

const searchIndices = {
  "by_omp": {
    "723": {"id": "OG-WRL-001", "name": "Communications Security (COMSEC) Management"},
    "752": {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning"},
    "751": {"id": "OG-WRL-003", "name": "Cybersecurity Workforce Management"},
    "652": {"id": "DD-WRL-001", "name": "Cybersecurity Architecture"}
  },
  "by_wrl": {
    "OG-WRL-001": {"id": "OG-WRL-001", "name": "Communications Security (COMSEC) Management"},
    "OG-WRL-002": {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning"},
    "OG-WRL-003": {"id": "OG-WRL-003", "name": "Cybersecurity Workforce Management"},
    "DD-WRL-001": {"id": "DD-WRL-001", "name": "Cybersecurity Architecture"}
  },
  "by_name": {
    "communications security (comsec) management": {"id": "OG-WRL-001", "name": "Communications Security (COMSEC) Management"},
    "cybersecurity policy and planning": {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning"},
    "cybersecurity workforce management": {"id": "OG-WRL-003", "name": "Cybersecurity Workforce Management"},
    "cybersecurity architecture": {"id": "DD-WRL-001", "name": "Cybersecurity Architecture"}
  }
};

// Application state
let currentRole = null;
let currentSuggestionIndex = -1;

// DOM elements
const searchInput = document.getElementById('searchInput');
const clearSearchBtn = document.getElementById('clearSearch');
const searchSuggestions = document.getElementById('searchSuggestions');
const loadingState = document.getElementById('loadingState');
const errorState = document.getElementById('errorState');
const roleDisplay = document.getElementById('roleDisplay');
const emptyState = document.getElementById('emptyState');

// Role display elements
const roleCategoryBadge = document.getElementById('roleCategoryBadge');
const roleOmpId = document.getElementById('roleOmpId');
const roleWrlId = document.getElementById('roleWrlId');
const roleName = document.getElementById('roleName');
const roleCategoryDescription = document.getElementById('roleCategoryDescription');
const tksRelatedList = document.getElementById('tksRelatedList');
const onRampsList = document.getElementById('onRampsList');
const offRampsList = document.getElementById('offRampsList');
const secondaryRolesList = document.getElementById('secondaryRolesList');

// Initialize application
document.addEventListener('DOMContentLoaded', function() {
  initializeEventListeners();
  handleInitialLoad();
});

function initializeEventListeners() {
  // Search input events
  searchInput.addEventListener('input', handleSearchInput);
  searchInput.addEventListener('keydown', handleSearchKeydown);
  searchInput.addEventListener('blur', hideSuggestions);
  
  // Clear search button
  clearSearchBtn.addEventListener('click', clearSearch);
  
  // Example search buttons
  const exampleBtns = document.querySelectorAll('.example-btn');
  exampleBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      const searchTerm = this.getAttribute('data-search');
      searchInput.value = searchTerm;
      performSearch(searchTerm);
    });
  });

  // Browser history
  window.addEventListener('popstate', handleHistoryChange);
}

function handleInitialLoad() {
  const urlParams = new URLSearchParams(window.location.search);
  const roleId = urlParams.get('role');
  
  if (roleId) {
    const role = findRoleById(roleId);
    if (role) {
      displayRole(role);
      searchInput.value = role.name;
    } else {
      showEmptyState();
    }
  } else {
    showEmptyState();
  }
}

function handleSearchInput(event) {
  const query = event.target.value.trim();
  
  if (query.length === 0) {
    hideSuggestions();
    return;
  }
  
  if (query.length >= 2) {
    showSuggestions(query);
  }
}

function handleSearchKeydown(event) {
  const suggestions = document.querySelectorAll('.suggestion-item');
  
  switch (event.key) {
    case 'Enter':
      event.preventDefault();
      if (currentSuggestionIndex >= 0 && suggestions[currentSuggestionIndex]) {
        const roleId = suggestions[currentSuggestionIndex].getAttribute('data-role-id');
        selectRole(roleId);
      } else {
        performSearch(searchInput.value.trim());
      }
      break;
      
    case 'ArrowDown':
      event.preventDefault();
      currentSuggestionIndex = Math.min(currentSuggestionIndex + 1, suggestions.length - 1);
      updateSuggestionSelection(suggestions);
      break;
      
    case 'ArrowUp':
      event.preventDefault();
      currentSuggestionIndex = Math.max(currentSuggestionIndex - 1, -1);
      updateSuggestionSelection(suggestions);
      break;
      
    case 'Escape':
      hideSuggestions();
      break;
  }
}

function showSuggestions(query) {
  const suggestions = searchForRoles(query);
  
  if (suggestions.length === 0) {
    hideSuggestions();
    return;
  }
  
  const html = suggestions.map(suggestion => 
    `<div class="suggestion-item" data-role-id="${suggestion.id}">
      <div class="suggestion-name">${suggestion.name}</div>
      <div class="suggestion-details">
        OMP: ${suggestion.omp.join(', ')} | WRL: ${suggestion.id}
      </div>
    </div>`
  ).join('');
  
  searchSuggestions.innerHTML = html;
  searchSuggestions.classList.remove('hidden');
  
  // Add click listeners to suggestions
  const suggestionItems = searchSuggestions.querySelectorAll('.suggestion-item');
  suggestionItems.forEach(item => {
    item.addEventListener('mousedown', function(event) {
      event.preventDefault(); // Prevent blur event
      const roleId = this.getAttribute('data-role-id');
      selectRole(roleId);
    });
  });
  
  currentSuggestionIndex = -1;
}

function updateSuggestionSelection(suggestions) {
  suggestions.forEach((item, index) => {
    if (index === currentSuggestionIndex) {
      item.classList.add('selected');
    } else {
      item.classList.remove('selected');
    }
  });
}

function hideSuggestions() {
  setTimeout(() => {
    searchSuggestions.classList.add('hidden');
    currentSuggestionIndex = -1;
  }, 150);
}

function clearSearch() {
  searchInput.value = '';
  hideSuggestions();
  showEmptyState();
  updateURL(null);
}

function searchForRoles(query) {
  const normalizedQuery = query.toLowerCase();
  const results = [];
  
  // Search by exact OMP ID
  if (searchIndices.by_omp[normalizedQuery]) {
    const result = searchIndices.by_omp[normalizedQuery];
    const role = findRoleById(result.id);
    if (role) results.push(role);
  }
  
  // Search by exact WRL ID
  const upperQuery = query.toUpperCase();
  if (searchIndices.by_wrl[upperQuery]) {
    const result = searchIndices.by_wrl[upperQuery];
    const role = findRoleById(result.id);
    if (role && !results.find(r => r.id === role.id)) results.push(role);
  }
  
  // Search by name (exact match first)
  if (searchIndices.by_name[normalizedQuery]) {
    const result = searchIndices.by_name[normalizedQuery];
    const role = findRoleById(result.id);
    if (role && !results.find(r => r.id === role.id)) results.push(role);
  }
  
  // Search by partial name match
  appData.work_roles.forEach(role => {
    if (role.name.toLowerCase().includes(normalizedQuery) && 
        !results.find(r => r.id === role.id)) {
      results.push(role);
    }
  });
  
  return results.slice(0, 5); // Limit to 5 suggestions
}

function performSearch(query) {
  if (!query) {
    showErrorState();
    return;
  }
  
  showLoadingState();
  
  setTimeout(() => {
    const results = searchForRoles(query);
    
    if (results.length > 0) {
      selectRole(results[0].id);
    } else {
      showErrorState();
    }
  }, 300);
}

function selectRole(roleId) {
  const role = findRoleById(roleId);
  
  if (role) {
    displayRole(role);
    searchInput.value = role.name;
    hideSuggestions();
    updateURL(roleId);
  } else {
    showErrorState();
  }
}

function findRoleById(id) {
  return appData.work_roles.find(role => role.id === id);
}

function displayRole(role) {
  currentRole = role;
  
  // Hide other states
  hideAllStates();
  roleDisplay.classList.remove('hidden');
  
  // Update role card
  const category = appData.categories[role.category];
  roleCategoryBadge.textContent = category.name;
  roleCategoryBadge.className = `role-category-badge ${category.class}`;
  
  roleOmpId.textContent = `OMP: ${role.omp.join(', ')}`;
  roleWrlId.textContent = `WRL: ${role.id}`;
  roleName.textContent = role.name;
  roleCategoryDescription.textContent = category.name;
  
  // Display DCWF information if available
  const dcwfInfo = document.getElementById('dcwfInfo');
  const dcwfOpmId = document.getElementById('dcwfOmpId');
  const dcwfTitle = document.getElementById('dcwfTitle');
  const dcwfDescription = document.getElementById('dcwfDescription');
  
  if (role.dcwf_info) {
    dcwfOpmId.textContent = role.dcwf_info.opm_id;
    dcwfTitle.textContent = role.dcwf_info.dcwf_title;
    dcwfDescription.textContent = role.dcwf_info.dcwf_description;
    dcwfInfo.classList.remove('hidden');
  } else {
    dcwfInfo.classList.add('hidden');
  }
  
  // Update relationship panels
  displayRelationshipList(tksRelatedList, role.tks_related, true);
  displayRelationshipList(onRampsList, role.on_ramps, true); // Show percentages for on_ramps
  displayRelationshipList(offRampsList, role.off_ramps, true); // Show percentages for off_ramps
  displayRelationshipList(secondaryRolesList, role.secondary_roles, true);
}

function displayRelationshipList(container, relationships, showPercentage) {
  if (!relationships || relationships.length === 0) {
    container.innerHTML = '<div class="empty-relationships">Aucune relation trouvée</div>';
    return;
  }
  
  const html = relationships.map(rel => {
    const percentage = showPercentage && rel.percentage ? 
      `<span class="relationship-item-percentage">${rel.percentage}%</span>` : '';
    
    return `
      <div class="relationship-item" data-role-id="${rel.id}">
        <div class="relationship-item-info">
          <div class="relationship-item-id">${rel.id}</div>
          <div class="relationship-item-name">${rel.name}</div>
        </div>
        ${percentage}
      </div>
    `;
  }).join('');
  
  container.innerHTML = html;
  
  // Add click listeners
  const relationshipItems = container.querySelectorAll('.relationship-item');
  relationshipItems.forEach(item => {
    item.addEventListener('click', function() {
      const roleId = this.getAttribute('data-role-id');
      selectRole(roleId);
    });
  });
}

function showLoadingState() {
  hideAllStates();
  loadingState.classList.remove('hidden');
}

function showErrorState() {
  hideAllStates();
  errorState.classList.remove('hidden');
}

function showEmptyState() {
  hideAllStates();
  emptyState.classList.remove('hidden');
}

function hideAllStates() {
  loadingState.classList.add('hidden');
  errorState.classList.add('hidden');
  roleDisplay.classList.add('hidden');
  emptyState.classList.add('hidden');
}

function updateURL(roleId) {
  const url = new URL(window.location);
  
  if (roleId) {
    url.searchParams.set('role', roleId);
  } else {
    url.searchParams.delete('role');
  }
  
  window.history.pushState({roleId}, '', url);
}

function handleHistoryChange(event) {
  const roleId = event.state?.roleId;
  
  if (roleId) {
    const role = findRoleById(roleId);
    if (role) {
      displayRole(role);
      searchInput.value = role.name;
    }
  } else {
    showEmptyState();
    searchInput.value = '';
  }
}