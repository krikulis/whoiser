 #TODO: write implementation
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'ccwhois.verisign-grs.com'
    def parse_response(self, response):
        return response
