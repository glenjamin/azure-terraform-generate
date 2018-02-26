#!/usr/bin/env python3

import argparse
import importlib
import json
from collections import namedtuple
import re
import subprocess

import aztfgen.hcl


def main():
    options = parse_arguments()

    verify_login(options.subscription_id)

    tf_config = build_config(options)

    print(tf_config)


Options = namedtuple("Options", [
    "address", "resource_id",
    "resource_type", "resource_name",
    "subscription_id"
])
SUBSCRIPTION_REGEXP = re.compile(r"/subscriptions/(.+?)/")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Generate terraform config from Azure resources'
    )
    parser.add_argument("address",
                        help="The terraform address to generate the resource against"
                        )
    parser.add_argument("resource_id",
                        help="The Azure resource ID"
                        )
    args = parser.parse_args()

    resource_type, resource_name = args.address.split('.')

    match = SUBSCRIPTION_REGEXP.match(args.resource_id)
    if match is None:
        raise "Can't find subscription ID in resource ID"
    subscription_id = match.group(1)

    return Options(
        args.address,
        args.resource_id,
        resource_type,
        resource_name,
        subscription_id
    )


def verify_login(subscription_id):
    subprocess.run(
        "az account set --subscription '%s'" % subscription_id,
        shell=True, check=True
    )


def build_config(options):
    resource = lookup_resource_type(options.resource_type)

    details = fetch_details(resource.command, options.resource_id)

    return hcl.build(
        options.resource_type,
        options.resource_name,
        resource.build(details)
    )


def lookup_resource_type(resource_type):
    prefix = "azurerm_"
    if not resource_type.startswith(prefix):
        raise "Only %s resources are supported" % prefix
    type_name = resource_type[len(prefix):]
    return importlib.import_module("aztfgen.resources.%s" % type_name)


def fetch_details(command, resource_id):
    json_data = subprocess.run(
        command % resource_id,
        stdout=subprocess.PIPE, shell=True, check=True
    ).stdout.decode()

    return json.loads(json_data)


if __name__ == '__main__':
    main()
