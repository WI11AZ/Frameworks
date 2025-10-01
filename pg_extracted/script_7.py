# Create the complete data structure for the web application
app_data = {
    'work_roles': [],
    'categories': data['career_pathways']['categories']
}

# Convert all roles to a format suitable for the web app
for role in work_roles:
    details = get_role_details(role)
    
    # Enrich related role data with names
    tks_related_enriched = []
    for tks in details['tks_related']:
        related_role = wrl_to_role.get(tks['text'])
        tks_related_enriched.append({
            'id': tks['text'],
            'name': related_role['name'] if related_role else 'Unknown Role',
            'percentage': tks['percentage']
        })
    
    on_ramps_enriched = []
    for ramp in details['on_ramps']:
        related_role = wrl_to_role.get(ramp)
        on_ramps_enriched.append({
            'id': ramp,
            'name': related_role['name'] if related_role else 'Unknown Role'
        })
    
    off_ramps_enriched = []
    for ramp in details['off_ramps']:
        related_role = wrl_to_role.get(ramp)
        off_ramps_enriched.append({
            'id': ramp,
            'name': related_role['name'] if related_role else 'Unknown Role'
        })
        
    secondary_roles_enriched = []
    for secondary in details['secondary_roles']:
        related_role = wrl_to_role.get(secondary['text'])
        secondary_roles_enriched.append({
            'id': secondary['text'],
            'name': related_role['name'] if related_role else 'Unknown Role',
            'percentage': secondary['percentage']
        })
    
    role_data = {
        'id': role['id'],
        'name': role['name'], 
        'opm': role.get('opm', []),
        'category': role['cid'],
        'tks_related': tks_related_enriched,
        'on_ramps': on_ramps_enriched,
        'off_ramps': off_ramps_enriched,
        'secondary_roles': secondary_roles_enriched
    }
    
    app_data['work_roles'].append(role_data)

# Create search indices for the app
search_indices = {
    'by_opm': {},
    'by_wrl': {},
    'by_name': {}
}

for role in app_data['work_roles']:
    # OPM index
    for omp_id in role['omp']:
        search_indices['by_opm'][omp_id] = role
    
    # WRL index
    search_indices['by_wrl'][role['id']] = role
    
    # Name index (both exact and keywords)
    search_indices['by_name'][role['name'].lower()] = role
    # Add keywords for partial matching
    words = role['name'].lower().replace('-', ' ').replace('(', '').replace(')', '').split()
    for word in words:
        if len(word) > 2:  # Only index meaningful words
            if word not in search_indices['by_name']:
                search_indices['by_name'][word] = []
            if isinstance(search_indices['by_name'][word], list):
                search_indices['by_name'][word].append(role)
            else:
                search_indices['by_name'][word] = [search_indices['by_name'][word], role]

print(f"Prepared data for {len(app_data['work_roles'])} work roles")
print(f"Categories: {list(app_data['categories'].keys())}")
print(f"Search indices: OPM={len(search_indices['by_omp'])}, WRL={len(search_indices['by_wrl'])}, Name keys={len(search_indices['by_name'])}")

# Save the data for the web app
import json
with open('ncwf_data.json', 'w', encoding='utf-8') as f:
    json.dump({
        'app_data': app_data,
        'search_indices': search_indices
    }, f, indent=2, ensure_ascii=False)

print("Data saved to ncwf_data.json")