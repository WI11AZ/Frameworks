# Test with the examples given
test_cases = [
    ("751", "opm"),
    ("DD-WRL-001", "wrl"), 
    ("cybersecurity workforce management", "name")
]

def find_role(input_value, input_type=None):
    """Find a role by OPM ID, WRL ID, or name"""
    role = None
    
    # Try to auto-detect input type if not specified
    if input_type is None:
        if input_value.isdigit():
            input_type = "opm"
        elif input_value.upper().startswith(('DD-', 'OG-', 'IO-', 'PD-', 'IN-')) and 'WRL' in input_value.upper():
            input_type = "wrl"
        else:
            input_type = "name"
    
    # Find the role based on input type
    if input_type == "opm":
        role = opm_to_role.get(str(input_value))
    elif input_type == "wrl":
        role = wrl_to_role.get(input_value.upper())
    elif input_type == "name":
        role = name_to_role.get(input_value.lower())
        # Also try partial matching for names
        if not role:
            for name, r in name_to_role.items():
                if input_value.lower() in name or name in input_value.lower():
                    role = r
                    break
    
    if role:
        return {
            "opm_id": role.get('opm', []),
            "wrl_id": role['id'], 
            "name": role['name'],
            "role_data": role
        }
    return None

# Test the examples
for test_input, expected_type in test_cases:
    print(f"\nTesting: '{test_input}' (expected type: {expected_type})")
    result = find_role(test_input)
    if result:
        print(f"✓ Found role:")
        print(f"  OPM ID: {result['opm_id']}")
        print(f"  WRL ID: {result['wrl_id']}")
        print(f"  Name: {result['name']}")
    else:
        print("✗ Role not found")