
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'whois.nic.ac'
    def parse_response(self, response):
        """ .ac whois registry only contains information about domain availability """
        if 'Not available' in response:
            available = False
        else:
            available = True
        return {'available' : available}
