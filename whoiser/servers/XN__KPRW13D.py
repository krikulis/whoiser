 #TODO: write implementation
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'whois.twnic.net.tw'
    def parse_response(self, response):
        return response
