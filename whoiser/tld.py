import iana
import urllib

__IANA_TLD_LIST = 'http://data.iana.org/TLD/tlds-alpha-by-domain.txt' 

def get_tld_list():
    request = urllib.urlopen(__IANA_TLD_LIST)
    response = request.read()
    tld_list = []
    for line in response.split("\n"):
        if line and not line.startswith("#"):
            tld_list.append(line)
    return tld_list

def get_whois_list():
    query = iana.IanaWhoisQuery()
    whois_servers = []
    for tld in get_tld_list():
        print "getting info for %s " % (tld)
        response = query.query(tld)
        if 'whois' in response:
            whois_servers.append((tld, response['whois']))
        else:
            whois_servers.append((tld, None))
    return whois_servers
