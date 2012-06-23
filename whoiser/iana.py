from whois import WhoisQuery

class IanaWhoisQuery(WhoisQuery):
    server = 'whois.iana.org'
    def parse_response(self,data):
        data = data.split("\n")
        response = {}
        for line in data:
            line = line.split(":")
            if len(line) != 2:
                continue
            response[line[0].strip(" ")] = line[1].strip(" ")
        return response
