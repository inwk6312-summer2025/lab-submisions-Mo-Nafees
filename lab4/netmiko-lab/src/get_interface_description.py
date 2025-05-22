from netmiko import ConnectHandler

# Define each router individually
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

# Loop through each router
for device in (r1, r2, r3):
    try:
        net_connect = ConnectHandler(**device)
        output = net_connect.send_command("show interface description")
        net_connect.disconnect()

        print(f"\n{'-'*100}")
        print(f"Interface Descriptions for {device['ip']}")
        print(output)
        print(f"{'-'*100}")
    except Exception as e:
        print(f"Failed to connect to {device['ip']}: {e}")

# List of show commands to run on each device
show_commands = [
    "show interface description",
    "show ip interface brief",
    "show version",
    "show running-config | include hostname",
    "show cdp neighbors",
    "show vlan brief"  # Optional: skip if not using VLANs
]

# Loop through each router and run commands
for device in (r1, r2, r3):
    try:
        print(f"\n{'='*100}")
        print(f"Connecting to {device['ip']}")
        net_connect = ConnectHandler(**device)

        for command in show_commands:
            print(f"\n--- Output of '{command}' on {device['ip']} ---")
            output = net_connect.send_command(command)
            print(output)

        net_connect.disconnect()
        print(f"{'='*100}\n")

    except Exception as e:
        print(f"Failed to connect to {device['ip']}: {e}")
