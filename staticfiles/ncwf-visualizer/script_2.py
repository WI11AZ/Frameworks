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
    
    # Map each OPM ID to role
    for omp_id in opm_ids:
        opm_to_role[omp_id] = role

print(f"Created mappings for {len(work_roles)} work roles")
print(f"OPM mappings: {len(opm_to_role)}")
print(f"WRL mappings: {len(wrl_to_role)}")
print(f"Name mappings: {len(name_to_role)}")

# Test with the example given (OPM 751)
test_opm = "751"
if test_omp in opm_to_role:
    role = opm_to_role[test_omp]
    print(f"\nTest OPM {test_opm}:")
    print(f"OPM ID: {test_opm}")
    print(f"WRL ID: {role['id']}")
    print(f"Name: {role['name']}")
else:
    print(f"OPM {test_opm} not found")