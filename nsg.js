const exec = require('child_process').execSync;

const tfname = process.argv[2];
const id = process.argv[3];

const subscription = /\/subscriptions\/(.+?)\//.exec(id)[1];

// Verify that we can log in
exec(`az account get-access-token --subscription "${subscription}"`);

// Grab NSG details
const show = exec(
  `az network nsg show --ids "${id}"`,
  {
    encoding: 'utf8'
  }
);

const details = JSON.parse(show);

const config = {
  resource: { azurerm_network_security_group: {
    [tfname]: {
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
        priority: rule.priority,
        direction: rule.direction,
      }))
    }
  }}
};

console.log(JSON.stringify(config, null, 2));
