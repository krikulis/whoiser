 #TODO: write implementation
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'whois.kenic.or.ke'
    def parse_response(self, response):
        return response
