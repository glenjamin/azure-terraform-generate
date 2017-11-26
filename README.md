# Azure Terraform Generate

Generate terraform config from deployed azure resources.

## Work in progress

This is currently just a proof of concept type thing.

## Usage

```
node nsg.js <terraform-name> <resourceid>
```

## HCL

This script outputs JSON, as that's easier to do. You can use [json2hcl](https://github.com/kvz/json2hcl) to make it into pretty HCL if you want.
