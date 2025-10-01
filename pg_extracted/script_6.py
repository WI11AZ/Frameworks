# Let's also get detailed information about related roles, on/off ramps, etc.
def get_role_details(role_data):
    """Extract detailed role information including relationships"""
    
    # Get TKS related roles (top5 ks-all data)
    tks_related = []
    if 'top5' in role_data and 'ks-all' in role_data['top5']:
        tks_related = role_data['top5']['ks-all']
    
    # Get on/off ramps
    on_ramps = role_data.get('ramps', {}).get('on', [])
    off_ramps = role_data.get('ramps', {}).get('off', [])
    
    # Get secondary work roles (from top5 roles)
    secondary_roles = []
    if 'top5' in role_data and 'roles' in role_data['top5']:
        secondary_roles = role_data['top5']['roles']
    
    return {
        'tks_related': tks_related,
        'on_ramps': on_ramps,
        'off_ramps': off_ramps,
        'secondary_roles': secondary_roles
    }

# Test with DD-WRL-001
test_role = find_role("DD-WRL-001")
if test_role:
    print(f"Role: {test_role['name']} ({test_role['wrl_id']})")
    details = get_role_details(test_role['role_data'])
    
    print(f"\nTKS Related Roles ({len(details['tks_related'])}):")
    for tks in details['tks_related'][:5]:  # Show top 5
        related_role = wrl_to_role.get(tks['text'])
        if related_role:
            print(f"  - {tks['text']}: {related_role['name']} ({tks['percentage']}%)")
        else:
            print(f"  - {tks['text']}: Unknown role ({tks['percentage']}%)")
    
    print(f"\nOn Ramps ({len(details['on_ramps'])}):")
    for ramp in details['on_ramps']:
        related_role = wrl_to_role.get(ramp)
        if related_role:
            print(f"  - {ramp}: {related_role['name']}")
        else:
            print(f"  - {ramp}: Unknown role")
    
    print(f"\nOff Ramps ({len(details['off_ramps'])}):")
    for ramp in details['off_ramps']:
        related_role = wrl_to_role.get(ramp)
        if related_role:
            print(f"  - {ramp}: {related_role['name']}")
        else:
            print(f"  - {ramp}: Unknown role")
    
    print(f"\nSecondary Work Roles ({len(details['secondary_roles'])}):")
    for secondary in details['secondary_roles'][:5]:  # Show top 5
        related_role = wrl_to_role.get(secondary['text'])
        if related_role:
            print(f"  - {secondary['text']}: {related_role['name']} ({secondary['percentage']}%)")
        else:
            print(f"  - {secondary['text']}: Unknown role ({secondary['percentage']}%)")