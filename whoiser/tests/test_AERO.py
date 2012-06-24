
import unittest
from servers.AERO import WhoisQuery

class TestAERO(unittest.TestCase):
    def setUp(self):
        self.query = WhoisQuery()
    def test_available(self):
        """ test available .aero domain name """
        response = self.query.query("whois.aero")
        expected = {'Registrant Street2': [''], 'Registrant Street3': [''], 'Updated On': ['06-Apr-2012 06:35:02 UTC'], 'Registrant Street1': ['26 chemin de Joinville'], 'Registrant Postal Code': ['CH-1216'], 'Admin Country': ['CH'], 'Registrant Organization': ['SITA SC'], 'Admin State/Province': ['GE'], 'Registrant Name': ['.aero Office'], 'Admin Organization': ['SITA SC'], 'Admin Phone Ext.': [''], 'Admin ID': ['C223523-AERO'], 'Tech Organization': ['CORE Internet Council of Registrars'], 'Sponsoring Registrar': ['SITA (9999)'], 'ENS_AuthId': ['E00001-SITA'], 'Billing State/Province': ['GE'], 'Registrant FAX': ['+41.227476333'], 'Admin Name': ['.aero Office'], 'Tech Email': ['werner.staub@corenic.org'], 'Billing Street1': ['26 chemin de Joinville'], 'Billing Name': ['.aero Office'], 'Billing Street3': [''], 'Billing Street2': [''], 'Billing Country': ['CH'], 'Tech Street3': [''], 'Registrant ID': ['C223523-AERO'], 'Billing Postal Code': ['CH-1216'], 'Billing Phone Ext.': [''], 'Admin FAX Ext.': [''], 'Admin Street2': [''], 'Admin City': ['Geneva'], 'Billing ID': ['C223523-AERO'], 'Tech Country': ['CH'], 'Tech FAX Ext.': [''], 'Tech FAX': ['+41.229295743'], 'Billing Phone': ['+41.227476000'], 'Updated By': ['Afilias Internal (984)'], 'Registrant Email': ['aero.enquiries@sita.aero'], 'Admin Street3': [''], 'Registrant Phone Ext.': [''], 'Admin Street1': ['26 chemin de Joinville'], '\n': [''], 'Admin Email': ['aero.enquiries@sita.aero'], 'Domain ID': ['D322-AERO'], 'Billing FAX': ['+41.227476333'], 'Expires On': ['05-Apr-2013 16:00:40 UTC'], 'Admin Phone': ['+41.227476000'], 'Registrant City': ['Geneva'], 'Tech Phone': ['+41.229295744'], 'Billing Email': ['aero.enquiries@sita.aero'], 'Created By': ['SITA (9999)'], 'Registrant State/Province': ['GE'], 'Tech Name': ['Werner Staub'], 'Billing FAX Ext.': [''], 'Registrant Phone': ['+41.227476000'], 'Tech City': ['Geneva'], 'Admin Postal Code': ['CH-1216'], 'Name Server': ['NS1.AMS1.AFILIAS-NST.INFO', 'NS1.HKG1.AFILIAS-NST.INFO', 'NS1.MIA1.AFILIAS-NST.INFO', 'NS1.SEA1.AFILIAS-NST.INFO', 'NS1.YYZ1.AFILIAS-NST.INFO', '', '', '', '', '', '', '', ''], 'Tech Postal Code': ['CH-1215'], 'Maintainer': ['http://www.sita.aero'], 'Billing City': ['Geneva'], 'Domain Status': ['OK'], 'Registrant FAX Ext.': [''], 'Created On': ['05-Apr-2002 15:00:40 UTC'], 'Billing Organization': ['SITA SC'], 'Tech Phone Ext.': [''], 'Tech Street2': [''], 'Tech ID': ['C223858-AERO'], 'Tech Street1': ['29 route de Pre-Bois'], 'Registrant Country': ['CH'], 'Admin FAX': ['+41.227476333'], 'Tech State/Province': ['GE'], 'Domain Name': ['WHOIS.AERO']}

        self.assertEqual(self.query.available, True)
        self.assertEqual(response, expected) 
    def test_unavailable(self):
        """ test unavailable .ae domain name """ 
        response = self.query.query("kristaps.aero")
        self.assertEqual(self.query.available, False)
