 #TODO: write implementation
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'tvwhois.verisign-grs.com'
    def parse_response(self, response):
        return response
