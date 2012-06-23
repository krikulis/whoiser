 #TODO: write implementation
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'whois.dk-hostmaster.dk'
    def parse_response(self, response):
        return response
