import unittest
from servers.AE import WhoisQuery

class TestAE(unittest.TestCase):
    def setUp(self):
        self.query = WhoisQuery()
    def test_available(self):
        """ test available .ae domain name """
        response = self.query.query("net.ae")
        expected = {'Status': ['ok'], 'Name Server': ['ns1.aedns.ae', 'ns2.aedns.ae', 'ns3.ausregistry.net.au', 'ns1.ausregistry.net.au', 'ns2.ausregistry.net.au', 'ns4.ausregistry.net.au'], 'Tech Contact Name': ['aeDA Registry'], 'Tech Contact Email': ['Visit whois.aeda.ae for Web based WhoIs'], 'Registrant Contact ID': ['AEDA REGISTRY'], 'Registrar ID': ['aeDA Registry'], 'Registrar Name': ['aeDA Registry'], 'Tech Contact ID': ['AEDA REGISTRY'], 'Registrant Contact Name': ['aeDA Registry'], 'Registrant Contact Email': ['Visit whois.aeda.ae for Web based WhoIs'], 'Domain Name': ['net.ae']}
        self.assertEqual(response, expected)
        self.assertEqual(self.query.available, True)
    def test_unavailable(self):
        """ test unavailable .ae domain name """ 
        response = self.query.query("kristaps.ae")
        self.assertEqual(self.query.available, False)
