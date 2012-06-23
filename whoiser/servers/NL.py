 #TODO: write implementation
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'whois.domain-registry.nl'
    def parse_response(self, response):
        return response
