// This is not a general purpose HCL formatter
// We know we're only doing a single resource
// And we also know we can rely on `terraform fmt` to tidy up after us

exports.buildHcl = function buildHcl(resourceType, name, resource) {
  const lines = [];

  lines.push(`resource ${value(resourceType)} ${value(name)} {`);
  lines.push(objectProperties(resource));
  lines.push('}');

  return lines.join("\n");

  function objectProperties(obj) {
    Object.keys(obj).forEach(key => {
      const val = obj[key];
      const type = typeof val;
      if (['number', 'string', 'boolean'].includes(type)) {
        primitve(key, val);
      } else if (!val) {
        primitve(key, "");
      } else if (Array.isArray(val)) {
        val.forEach((item) => object(key, item));
      } else {
        object(key, val);
      }
    });
  }
  function primitve(key, val) {
    lines.push(`${key} = ${value(val)}`);
  }
  function object(key, val) {
    lines.push(`${key} {`);
    lines.push(objectProperties(val));
    lines.push(`}`);
  }
  function value(val) {
    return JSON.stringify(val);
  }
}
