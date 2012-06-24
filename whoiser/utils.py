def make_py_namespace(name):
    """ make valid python namespace name from string """
    return name.replace("-", "_")

def make_py_filename(name):
    """ make python filename from string """ 
    return "%s.py" % make_py_namespace(name)

def string_to_dict(string, line_seperator = "\n", value_seperator = ":"):
    lines = string.split(line_seperator)
    response = {}
    for line in lines:
        if line.strip(" ") == "":
            continue
        line = line.strip(" ")
        line = line.split(value_seperator)
        key = line.pop(0).strip(" ")
        value = value_seperator.join(line).strip(" ")
        if key in response:
            response[key].append(value)
        else:
            response[key] = [value]
    return response
