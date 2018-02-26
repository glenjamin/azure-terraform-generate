from collections import OrderedDict as OD

command = "az network nsg show --ids '%s'"


def build(details):
    return OD([
        ("name", details["name"]),
        ("location", details["location"]),
        ("resource_group_name", details["resourceGroup"]),
        ("tags", details["tags"]),
        ("security_rule", [OD([
            ("name", rule["name"]),
            ("description", rule.get("description", "")),
            ("priority", rule["priority"]),
            ("direction", rule["direction"]),
            ("access", rule["access"]),
            ("protocol", rule["protocol"]),
            ("source_address_prefix", rule["sourceAddressPrefix"]),
            ("source_port_range", rule["sourcePortRange"]),
            ("destination_address_prefix", rule["destinationAddressPrefix"]),
            ("destination_port_range", rule["destinationPortRange"]),
        ]) for rule in details["securityRules"]])
    ])
