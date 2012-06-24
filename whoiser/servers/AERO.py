from utils import string_to_dict
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    server = 'whois.aero'
    unavailable_key = "NOT FOUND\n"
    def parse_response(self, response):
        return response
