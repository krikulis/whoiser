 #TODO: write implementation
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'whois1.nic.bi'
    def parse_response(self, response):
        return response
