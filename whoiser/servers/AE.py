from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'whois.aeda.net.ae'
    unavailable_key = "No data found"
    def parse_response(self, response):
        return response
