 #TODO: write implementation
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'whois.afilias.net'
    def parse_response(self, response):
        return response
