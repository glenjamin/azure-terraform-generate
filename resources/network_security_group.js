exports.command = 'az network nsg show --ids "%s"';

exports.build = (details) => ({
  name: details.name,
  location: details.location,
  resource_group_name: details.resourceGroup,
  tags: details.tags,
  security_rule: details.securityRules.map((rule) => ({
    name: rule.name,
    description: rule.description || "",
    priority: rule.priority,
    protocol: rule.protocol,
    source_port_range: rule.sourcePortRange,
    destination_port_range: rule.destinationPortRange,
    source_address_prefix: rule.sourceAddressPrefix,
    destination_address_prefix: rule.destinationAddressPrefix,
    access: rule.access,
    direction: rule.direction,
  }))
});
