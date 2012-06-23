def make_py_namespace(name):

    return name.replace("-", "_")
def make_py_filename(name):
    return "%s.py" % make_py_namespace(name)
