# Create search indices for the app
search_indices = {
    'by_opm': {},
    'by_wrl': {},
    'by_name': {}
}

for role in app_data['work_roles']:
    # OPM index - now handle list properly
    for opm_id in role['opm']:
        search_indices['by_opm'][opm_id] = role
    
    # WRL index
    search_indices['by_wrl'][role['id']] = role
    
    # Name index (both exact and keywords)
    search_indices['by_name'][role['name'].lower()] = role

print(f"Search indices created successfully:")
print(f"  OPM mappings: {len(search_indices['by_opm'])}")
print(f"  WRL mappings: {len(search_indices['by_wrl'])}")
print(f"  Name mappings: {len(search_indices['by_name'])}")

# Save the final data structure
final_data = {
    'app_data': app_data,
    'search_indices': search_indices
}

# Convert to JSON for the web app
data_json = json.dumps(final_data, ensure_ascii=False, separators=(',', ':'))
print(f"JSON data prepared: {len(data_json)} characters")

# Test the search functionality
def test_app_search(query):
    print(f"\n=== Testing search for: '{query}' ===")
    
    # Auto-detect search type
    search_type = None
    result = None
    
    # Try OPM search first
    if query.isdigit():
        search_type = "OPM ID"
        result = search_indices['by_opm'].get(query)
    
    # Try WRL search
    if not result and query.upper().startswith(('DD-', 'OG-', 'IO-', 'PD-', 'IN-')):
        search_type = "WRL ID"
        result = search_indices['by_wrl'].get(query.upper())
    
    # Try exact name search
    if not result:
        search_type = "Role Name"
        result = search_indices['by_name'].get(query.lower())
    
    # Try partial name search
    if not result:
        search_type = "Partial Name"
        for name, role in search_indices['by_name'].items():
            if query.lower() in name or name in query.lower():
                result = role
                break
    
    if result:
        print(f"✓ Found by {search_type}:")
        print(f"  OPM ID: {result['opm']}")
        print(f"  WRL ID: {result['id']}")
        print(f"  Name: {result['name']}")
        print(f"  Category: {result['category']}")
        print(f"  TKS Related: {len(result['tks_related'])} roles")
        print(f"  On Ramps: {len(result['on_ramps'])} roles")
        print(f"  Off Ramps: {len(result['off_ramps'])} roles")
        print(f"  Secondary Roles: {len(result['secondary_roles'])} roles")
        return result
    else:
        print("✗ Not found")
        return None

# Test with the examples from the user request
test_app_search("751")
test_app_search("DD-WRL-001")
test_app_search("Cybersecurity Workforce Management")