
from servers.generic import GenericWhoisQuery
class WhoisQuery(GenericWhoisQuery):
    def query(self, query):
        raise NotImplementedError(u"TLD PA has no Whois server available")
