# Fix typo and debug the issue
for i, role in enumerate(work_roles[:3]):
    print(f"Role {i}: {role['name']}")
    opm_field = role.get('opm', None)
    print(f"  opm field type: {type(opm_field)}, value: {opm_field}")
    print()

# Create a mapping for faster lookups
opm_to_role = {}
wrl_to_role = {}
name_to_role = {}

for role in work_roles:
    wrl_id = role['id']
    role_name = role['name']
    opm_ids = role.get('opm', [])
    
    # Map WRL ID to role
    wrl_to_role[wrl_id] = role
    
    # Map role name to role (normalize for better matching)
    name_to_role[role_name.lower()] = role
    
    # Map each OPM ID to role - handle the case where opm_ids might not be a list
    if isinstance(opm_ids, list):
        for opm_id in opm_ids:
            opm_to_role[opm_id] = role
    elif opm_ids:  # single value
        opm_to_role[str(opm_ids)] = role

print(f"Created mappings for {len(work_roles)} work roles")
print(f"OPM mappings: {len(opm_to_role)}")
print(f"WRL mappings: {len(wrl_to_role)}")
print(f"Name mappings: {len(name_to_role)}")