
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'whois.nic.ac'
    unavailable_key = "Not available"
    def parse_response(self, response):
        return response
    def check_available(self, response):
        if self.unavailable_key in self.raw_response:
            self.available = False
        else:
            self.available = True
