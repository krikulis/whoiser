
from servers import TLD_LIST

def get_whois_query(domain_name):
    """ get whois query for domain """ 
    domain_name = domain_name.split(".")
    domain_name.pop(0)
    domain_name = '.'.join(domain_name)
    whois = [whois for tld,whois in TLD_LIST if tld == domain_name.upper()]
    if len(whois) != 1:
        raise NotImplementedError("No such TLD %s " % domain_name)
    return whois[0]

