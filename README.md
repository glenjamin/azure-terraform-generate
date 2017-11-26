# Azure Terraform Generate

Generate terraform config from deployed azure resources.

Made a bunch of stuff in azure but wish you'd used terraform? Nows your chance to fix the mistakes of past-you.

## Work in progress

This is currently just a proof of concept type thing.

## Requirements

* Node.JS 8+
* The Azure 2.0 CLI (The python based `az` one).

In order to dodge API calling and avoid having to deal with azure authentication, this project abdicates all responsibility for that functionality by shelling out to the azure CLI.

## Install

I'll probably publish to npm when this is a bit more fully formed, for now you'll have to git clone.

## Usage

The arguments are intended to match whatever you'll also need to pass to `terraform import` to take care of getting the current state into terraform.

```
./aztfgen.js <terraform-address> <resource-id>
```
