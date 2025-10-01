import json

# Load the JSON data from the file
with open('ramp-on_off.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract work role data 
work_roles = data['career_pathways']['roles']

# Let's examine the structure of a few work roles to understand the data better
print("Number of work roles:", len(work_roles))
print("\nFirst work role example:")
print(json.dumps(work_roles[0], indent=2))

print("\n\nLet's see the OPM mapping for the first few roles:")
for i, role in enumerate(work_roles[:5]):
    print(f"Role {i}: {role['name']} - WRL ID: {role['id']} - OPM: {role['omp'] if 'opm' in role else role.get('omp', 'N/A')}")