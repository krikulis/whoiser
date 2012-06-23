 #TODO: write implementation
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'kero.yachay.pe'
    def parse_response(self, response):
        return response
