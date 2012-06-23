 #TODO: write implementation
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'whois.na-nic.com.na'
    def parse_response(self, response):
        return response
