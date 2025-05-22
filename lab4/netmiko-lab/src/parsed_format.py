from netmiko import Netmiko

# Define each router
r1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": 22
}

r2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.102",
    "username": "student",
    "password": "Meilab123",
    "port": 22
}

r3 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.103",
    "username": "student",
    "password": "Meilab123",
    "port": 22
}

# Loop through each router and parse 'show ip route'
for device in (r1, r2, r3):
    try:
        print(f"\n{'='*80}")
        print(f"Connecting to {device['ip']}...")

        net_connect = Netmiko(**device)
        output = net_connect.send_command("show ip route", use_textfsm=True)
        net_connect.disconnect()

        if not output:
            print(f"No routing entries found or parsing failed on {device['ip']}")
            continue

        print(f"Routing entries on {device['ip']}:")
        print(f"{'Protocol':<10} {'Network':<20} {'Distance':<10} {'Metric':<10}")
        print("-" * 60)

        for route in output:
            protocol = route.get('protocol', 'N/A')
            network = route.get('network', 'N/A')
            distance = route.get('distance', 'N/A')
            metric = route.get('metric', 'N/A')
            print(f"{protocol:<10} {network:<20} {distance:<10} {metric:<10}")

    except Exception as e:
        print(f"Error connecting to {device['ip']}: {e}")

