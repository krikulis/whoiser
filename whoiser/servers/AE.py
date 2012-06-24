
 #TODO: write implementation
from servers.generic import GenericWhoisQuery
from utils import string_to_dict 
class WhoisQuery(GenericWhoisQuery):
    server = 'whois.aeda.net.ae'
    def parse_response(self, response):
        response = string_to_dict(response, line_seperator = "\r\n")
        if 'No data found' in response:
            return {'available' : False}
        else:
            response['available'] = True
        return response
