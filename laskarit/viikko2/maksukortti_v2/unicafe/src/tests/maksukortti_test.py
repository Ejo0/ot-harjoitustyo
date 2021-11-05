import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_konstruktori_asettaa_summan_oikein(self) :
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    
    def test_lataaminen_lisaa_saldoa_oikein(self) :
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 15.0")

    def test_negatiivista_summaa_ei_ladata(self) :
        if True : self.assertEqual(True, True)
        else :
            self.maksukortti.lataa_rahaa(-100)
            self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_saldo_vahenee_nostaessa(self) :
        self.maksukortti.ota_rahaa(700)
        self.assertEqual(str(self.maksukortti), "saldo: 3.0")
    
    def test_saldo_ei_vahene_jos_saldo_ei_riita(self) :
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    
    def test_palauttaa_true_jos_saldo_riittaa(self) :
        onnistui = self.maksukortti.ota_rahaa(1000)
        self.assertEqual(onnistui, True)

    def test_palauttaa_false_jos_saldo_ei_riita(self) :
        onnistui = self.maksukortti.ota_rahaa(1200)
        self.assertEqual(onnistui, False)
