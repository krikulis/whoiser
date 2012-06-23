 #TODO: write implementation
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'cwhois.cnnic.cn'
    def parse_response(self, response):
        return response
