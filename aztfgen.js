#!/usr/bin/env node
const fmt = require('util').format;
const exec = require('child_process').execSync;

const {buildHcl} = require('./hcl');

main(process.argv);

function main(argv) {
  const {
    resourceType,
    resourceName,
    subscriptionId,
    resourceId,
    format,
  } = parseArguments(argv);

  verifyLogin(subscriptionId);

  const resource = lookupResourceType(resourceType);

  const details = fetchDetails(resource.command, resourceId);

  const config = {
    resource: {
      [resourceType]: {
        [resourceName]: resource.build(details)
      }
    }
  };

  const output = format(config);

  // eslint-disable-next-line no-console
  console.log(output);
}

function parseArguments(argv) {
  // TODO: yargs
  const address = argv[2];
  const resourceId = argv[3];

  const [resourceType, resourceName] = address.split(".");
  const subscriptionId = /\/subscriptions\/(.+?)\//.exec(resourceId)[1];

  const format = argv[4] === 'hcl' ? formatAsHcl : formatAsJson;

  return {resourceType, resourceName, subscriptionId, resourceId, format};
}

function verifyLogin(subscriptionId) {
  exec(`az account set --subscription "${subscriptionId}"`);
}

function lookupResourceType(resourceType) {
  const prefix = 'azurerm_';
  if (!resourceType.startsWith(prefix)) {
    throw new Error(`Only ${prefix} resources are supported`);
  }
  const type = resourceType.substring(prefix.length);
  return require(`./resources/${type}`);
}

function fetchDetails(command, id) {
  const output = exec(fmt(command, id), {encoding: 'utf8'});
  return JSON.parse(output);
}

function formatAsJson(config) {
  return JSON.stringify(config, null, 2);
}
function formatAsHcl(config) {

  const resourceType = firstKey(config.resource);
  const name = firstKey(config.resource[resourceType]);
  const resource = config.resource[resourceType][name];

  const hcl = buildHcl(resourceType, name, resource);

  return hcl;
}
function firstKey(obj) {
  return Object.keys(obj)[0];
}
