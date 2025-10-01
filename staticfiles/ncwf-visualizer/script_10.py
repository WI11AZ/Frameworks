# Fix the typo and debug
missing_opm = []
for role in work_roles:
    opm_field = role.get('opm', None)
    if not opm_field or not isinstance(opm_field, list):
        missing_opm.append(role)

print(f"Roles with missing or invalid opm data: {len(missing_opm)}")
if missing_opm:
    for role in missing_opm[:3]:
        print(f"  - {role['name']} ({role['id']}): opm = {role.get('opm', 'MISSING')}")

# Let's handle the OPM field more carefully
app_data = {
    'work_roles': [],
    'categories': data['career_pathways']['categories']
}

# Convert all roles to a format suitable for the web app
for role in work_roles:
    details = get_role_details(role)
    
    # Handle OPM field carefully
    omp_list = role.get('opm', [])
    if not isinstance(omp_list, list):
        omp_list = [str(omp_list)] if omp_list else []
    
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
        'opm': omp_list,
        'category': role['cid'],
        'tks_related': tks_related_enriched,
        'on_ramps': on_ramps_enriched,
        'off_ramps': off_ramps_enriched,
        'secondary_roles': secondary_roles_enriched
    }
    
    app_data['work_roles'].append(role_data)

print(f"Successfully prepared data for {len(app_data['work_roles'])} work roles")