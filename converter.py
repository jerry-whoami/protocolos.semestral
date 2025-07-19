import ipaddress

def ip_to_uint32(ip):
    return int(ipaddress.IPv4Address(ip))

# Example:
router_id = "3.3.3.3"
nbr_id = ip_to_uint32(router_id)
print(nbr_id)  # Output: 16843009

