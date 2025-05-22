from netmiko import Netmiko

# List of 3 Cisco routers
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": 22
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
        "port": 22
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",  # Third router
        "username": "student",
        "password": "Meilab123",
        "port": 22
    }
]

# Loop through all devices
for device in devices:
    try:
        net_connect = Netmiko(**device)
        output = net_connect.send_command("show version")
        net_connect.disconnect()

        # Search for Configuration Register line
        config_reg = None
        for line in output.splitlines():
            if "Configuration register is" in line:
                config_reg = line.strip()
                break

        if config_reg:
            print(f"{device['ip']} => {config_reg}")
        else:
            print(f"{device['ip']} => Configuration Register not found")

    except Exception as e:
        print(f"Failed to connect to {device['ip']}: {e}")
