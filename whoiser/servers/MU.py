 #TODO: write implementation
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'whois.nic.mu'
    def parse_response(self, response):
        return response