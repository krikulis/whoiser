''' Whois server abstractions '''
import socket

class WhoisQuery(object):
    server = None 
    port = 43
    def _open_connection(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.server, self.port))
    def _close_connection(self):
        self.socket.close()
    def query(self, query):
        self._open_connection()
        
        self.socket.send("%s\n" % query)
        response = [] 
        while True:
            data = self.socket.recv(1024)
            if not data:
                break
            response.append(data)
        self._close_connection()
        response = ''.join(response)
        self.parse_response(response)

