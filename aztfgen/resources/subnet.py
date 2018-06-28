from collections import OrderedDict as OD

command = "az network vnet subnet show --ids %s"

def itemId(details, name):
    try:
        return details[name]["id"]
    except (TypeError, KeyError):
        return None

def build(details):
    return OD([
        ("name", details["name"]),
        ("resource_group_name", details["resourceGroup"]),
        ("virtual_network_name", details["id"].rsplit("/", 3)[1]),
        ("address_prefix", details["addressPrefix"]),
        ("network_security_group_id", itemId(details, "networkSecurityGroup")),
        ("route_table_id", itemId(details,"routeTable")), 
        ("service_endpoints", [s["service"] for s in (details["serviceEndpoints"] or [])]),
    ])
