# Azure Terraform Generate

Generate terraform config from deployed azure resources.

Made a bunch of stuff in azure but wish you'd used terraform? Now's your chance to fix the mistakes of past-you.

## Work in progress

This is currently just a proof of concept type thing.

## Requirements

* Python 3.5+
* The Azure 2.0 CLI (The python based `az` one).

In order to dodge API calling and avoid having to deal with azure authentication, this project abdicates all responsibility for that functionality by shelling out to the azure CLI.

## Install

```sh
pip3 install aztfgen
```

## Usage

The arguments are intended to match whatever you'll also need to pass to `terraform import` to take care of getting the current state into terraform.

```
aztfgen <terraform-address> <resource-id>
```

### Importing lots of resources

If you want to do a bulk import, your best bet is to use a loop and some shell.

For example:

```
az network nsg list > nsgs.json
cat nsgs.json | jq 'map("aztfgen azurerm_network_security_group." + .name + " " + .id + " > " + .name + ".tf") | join("\n")' -r | bash -x
cat nsgs.json | jq 'map("terraform import azurerm_network_security_group." + .name + " " + .id) | join("\n")' -r | bash
```

## License

MIT
