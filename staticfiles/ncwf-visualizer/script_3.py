# Debug the issue - check what opm_ids actually contains
for i, role in enumerate(work_roles[:3]):
    print(f"Role {i}: {role['name']}")
    opm_field = role.get('opm', None)
    print(f"  opm field type: {type(omp_field)}, value: {omp_field}")
    print()