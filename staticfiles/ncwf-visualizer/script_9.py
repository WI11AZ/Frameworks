# Debug what's causing the issue with opm field
for i, role in enumerate(work_roles[:3]):
    print(f"Role {i}: {role['name']}")
    opm_field = role.get('opm', [])
    print(f"  opm field type: {type(opm_field)}, value: {opm_field}")
    if 'opm' not in role:
        print(f"  No opm field, available keys: {list(role.keys())}")
    print()

# Let's check if there are any roles missing opm data
missing_opm = []
for role in work_roles:
    omp_field = role.get('opm', None)
    if not omp_field or not isinstance(omp_field, list):
        missing_omp.append(role)

print(f"Roles with missing or invalid opm data: {len(missing_omp)}")
if missing_opm:
    for role in missing_opm[:3]:
        print(f"  - {role['name']} ({role['id']}): opm = {role.get('opm', 'MISSING')}")