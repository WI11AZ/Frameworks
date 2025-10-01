# Fix the typo and examine the data structure more carefully
print("First work role structure:")
print(json.dumps(work_roles[0], indent=2))

print("\nLet's see the OPM mapping for the first few roles:")
for i, role in enumerate(work_roles[:5]):
    opm_ids = role.get('omp', role.get('opm', 'N/A'))
    print(f"Role {i}: {role['name']} - WRL ID: {role['id']} - OPM: {opm_ids}")
    print(f"  On Ramps: {role.get('ramps', {}).get('on', [])}")
    print(f"  Off Ramps: {role.get('ramps', {}).get('off', [])}")
    print(f"  Secondary Roles (top5): {role.get('top5', {}).get('roles', [])}")
    print()