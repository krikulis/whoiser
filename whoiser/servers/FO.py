 #TODO: write implementation
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'whois.nic.fo'
    def parse_response(self, response):
        return response