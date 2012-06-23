import os 
from tld import get_whois_list
from string import Template
from utils import make_py_filename 
from utils import make_py_namespace
WHOIS_INTERFACE = """ #TODO: write implementation
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = '${server}'
    def parse_response(self, response):
        return response
"""
NO_WHOIS_INTERFACE = """
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    def query(self, query):
        raise NotImplementedError(u"TLD $tld has no Whois server available")
"""
WHOIS_TEMPLATE = Template(WHOIS_INTERFACE)
NO_WHOIS_TEMPLATE = Template(NO_WHOIS_INTERFACE)
MY_ROOT = os.path.dirname(os.path.realpath(__file__))

def get_implementation(tld, server):
    if server:
        return WHOIS_TEMPLATE.substitute(tld = tld, server = server)
    else:
        return NO_WHOIS_TEMPLATE.substitute(tld = tld)
def write_implementation(tld, code):
    filename = os.path.join(MY_ROOT, 'servers')
    filename = os.path.join(filename, make_py_filename(tld))
    print filename 
    f = open(filename, "w+")
    f.write(code)
    f.close() 
def write_tld_list(tld_list):
    imports = []
    code = [u"TLD_LIST = ["]
    for tld in tld_list:
        code.append('("%s", %s.WhoisQuery),' % (tld,make_py_namespace(tld)))
        imports.append(u"from servers import %s" % make_py_namespace(tld))
    code.append("]")
    imports.append("\n\n")
    code = u"\n".join(code)
    imports = u"\n".join(imports)
    filename = os.path.join(MY_ROOT, 'servers')
    filename = os.path.join(filename, "__init__.py")
    print filename
    f = open(filename, "w+")
    f.write(imports)
    f.write(code)
    f.close()
def update_implementations():
    tld_list = []
    for tld, server in get_whois_list():
        implementation = get_implementation(tld, server)
        write_implementation(tld, implementation)
        tld_list.append(tld)
    write_tld_list(tld_list)
update_implementations()
