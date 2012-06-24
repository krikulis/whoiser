import unittest
from servers.AC import WhoisQuery

class TestAC(unittest.TestCase):
    def setUp(self):
        self.query = WhoisQuery()
    def test_available(self):
        """ test available .ac domain name """
        response = self.query.query("kristaps.ac")
        self.assertEqual(response['available'], True)
    def test_unavailable(self):
        """ test unavailable .ac domain name """ 
        response = self.query.query("nic.ac")
        self.assertEqual(response['available'], False)
