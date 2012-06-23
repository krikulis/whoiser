 #TODO: write implementation
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'whois.tznic.or.tz'
    def parse_response(self, response):
        return response
