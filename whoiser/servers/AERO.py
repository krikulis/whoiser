
from utils import string_to_dict
from servers.generic import GenericWhoisQuery

_PREFIX = ["Access to .AERO WHOIS information is provided to assist persons in ",
            "determining the contents of a domain name registration record in the ",
"Afilias registry database. The data in this record is provided by ",
"Afilias Limited for informational purposes only, and Afilias does not ",
"guarantee its accuracy.  This service is intended only for query-based ",
"access. You agree that you will use this data only for lawful purposes ",
"and that, under no circumstances will you use this data to: (a) allow, ",
"enable, or otherwise support the transmission by e-mail, telephone, or ",
"facsimile of mass unsolicited, commercial advertising or solicitations ",
"to entities other than the data recipient's own existing customers; or ",
"(b) enable high volume, automated, electronic processes that send ",
"queries or data to the systems of Registry Operator, a Registrar, or ",
"Afilias except as reasonably necessary to register domain names or ",
"modify existing registrations. All rights reserved. Afilias reserves ",
"the right to modify these terms at any time. By submitting this query, ",
"you agree to abide by this policy."]
PREFIX = '\r\n'.join(_PREFIX)
class WhoisQuery(GenericWhoisQuery):
    server = 'whois.aero'
    unavailable_key = "NOT FOUND\n"
    prefix = PREFIX
    def parse_response(self, response):
        return response
