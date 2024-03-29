import re
import ipaddress

# Function to calculate the opposite end of the subnet
def calculate_opposite_end(ip, mask):
    network = ipaddress.IPv4Network(ip + '/' + mask, strict=False)
    opposite_end = network.network_address + (network.max_prefixlen - network.prefixlen) - 1
    return str(opposite_end)

# Read the interface.log file
with open('interface1.log', 'r') as file:
    log_data = file.read()

# Extract IPv4 addresses from descriptions containing "uT:"
pattern = re.findall(r'description uT:.*?ipv4 address (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', log_data, re.DOTALL)

# Ping each extracted IP with MTU 3000
for ip, mask in pattern:
    opposite_end = calculate_opposite_end(ip, mask)
    ping_command = f'ping {opposite_end} size 3000 repeat 1'
    print(ping_command)