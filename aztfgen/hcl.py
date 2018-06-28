import json


def build(resource_type, resource_name, resource):
    lines = []

    lines.append("resource %s %s {" %
        (value(resource_type), value(resource_name))
    )
    lines.extend(object_props(resource))
    lines.append("}")

    return "\n".join(lines)


def value(val):
    return json.dumps(val)


primitives = [int, float, str, bool]
def object_props(obj):
    lines = []

    for key, val in obj.items():
        val_type = type(val)
        if val_type in primitives:
            lines.append(primitve(key, val))
        elif val_type is list:
            if not val or type(val[0]) in primitives:
                lines.append(primitve(key, val))
            else:
                for item in val:
                    lines.extend(object(key, item))
        elif not val:
            lines.append(primitve(key, ""))
        else:
            lines.extend(object(key, val))

    return lines


def object(key, val):
    lines = []

    lines.append("%s {" % key)
    lines.extend(object_props(val))
    lines.append("}")

    return lines


def primitve(key, val):
    return "%s = %s" % (key, value(val))
