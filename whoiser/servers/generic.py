
''' Whois server abstractions '''
import socket
from utils import string_to_dict 

class GenericWhoisQuery(object):
    server = None 
    port = 43
    line_seperator = "\r\n"
    unavailable_key = ""
    prefix = ""
    def _open_connection(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.server, self.port))
    def _close_connection(self):
        self.socket.close()
    def query(self, query):
        self._open_connection()
        self.socket.send("%s%s" % (query, self.line_seperator))
        response = [] 
        while True:
            data = self.socket.recv(1024)
            if not data:
                break
            response.append(data)
        self._close_connection()
        response = ''.join(response)
        self.raw_response = response
        if response.startswith(self.prefix):
            response = response[len(self.prefix):]
        response = string_to_dict(response, line_seperator = self.line_seperator)
        self.check_available(response)
        return self.parse_response(response)
    def check_available(self, response):
        if self.unavailable_key == "":
            return 
        if self.unavailable_key in response:
            self.available = False
        else:
            self.available = True
