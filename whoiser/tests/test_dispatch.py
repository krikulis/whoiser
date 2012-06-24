from dispatch import get_whois_query
import unittest 

class TestGetWhoisQuery(unittest.TestCase):
    def test_valid_domain_name(self):
        from servers.LV import WhoisQuery
        query = get_whois_query("domain.lv")
        self.assertEqual(query, WhoisQuery)
    def test_valid_domain_name_with_mixed_case(self):
        from servers.COM import WhoisQuery
        query = get_whois_query("domain.cOm")
        self.assertEqual(query, WhoisQuery)
    def test_invalid_tld(self):
        self.assertRaises(NotImplementedError, 
                          get_whois_query, "do.nonexistent",)
