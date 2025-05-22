from netmiko import Netmiko
devices = [{"device_type": "cisco_ios",
	    "ip": "192.168.1.101",
	    "username": "student",
	    "password": "Meilab123",
	    "port": "22",}]
# Configuration commands to add Loopback10 interface
loopback_config = [
    "interface Loopback10",
    "ip address 10.10.10.10 255.255.255.255",
    "description Created via Netmiko script",
    "no shutdown"
]

for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_config_set(loopback_config)
    print(output)
    net_connect.disconnect()
