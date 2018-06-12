from collections import OrderedDict as OD

command = "az network vnet show --ids '%s'"

def build(details):
    return OD([
        ("name", details["name"]),
        ("location", details["location"]),
        ("resource_group_name", details["resourceGroup"]),
        ("tags", details["tags"] or {}),
        ("address_space", details["addressSpace"]["addressPrefixes"]),
        ("dns_servers", details["dhcpOptions"]["dnsServers"])
    ])
