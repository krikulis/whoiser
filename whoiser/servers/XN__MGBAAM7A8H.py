 #TODO: write implementation
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'whois.aeda.net.ae'
    def parse_response(self, response):
        return response
