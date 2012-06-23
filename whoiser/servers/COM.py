 #TODO: write implementation
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'whois.verisign-grs.com'
    def parse_response(self, response):
        return response
