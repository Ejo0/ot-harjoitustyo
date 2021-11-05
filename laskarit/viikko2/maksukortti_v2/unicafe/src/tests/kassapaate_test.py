import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase) :

    def setUp(self) -> None:
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)
    
    def test_konstruktori_asettaa_oikeat_arvot(self) :
        rahaa = self.kassa.kassassa_rahaa
        edulliset = self.kassa.edulliset
        maukkaat = self.kassa.maukkaat
        self.assertEqual((rahaa, edulliset, maukkaat), (100_000, 0, 0))

    def test_syo_edullisesti_kateisella_antaa_oikeat_arvot(self) :
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(300)
        kassassa_rahaa = self.kassa.kassassa_rahaa
        edulliset = self.kassa.edulliset
        self.assertEqual((vaihtoraha, kassassa_rahaa, edulliset), (60, 100_240, 1))

    def test_syo_edullisesti_kateisella_alle_hinnan_antaa_oikeat_arvot(self) :
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(200)
        kassassa_rahaa = self.kassa.kassassa_rahaa
        edulliset = self.kassa.edulliset
        self.assertEqual((vaihtoraha, kassassa_rahaa, edulliset), (200, 100_000, 0))
    
    def test_syo_maukkaasti_kateisella_antaa_oikeat_arvot(self) :
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(500)
        kassassa_rahaa = self.kassa.kassassa_rahaa
        maukkaat = self.kassa.maukkaat
        self.assertEqual((vaihtoraha, kassassa_rahaa, maukkaat), (100, 100_400, 1))

    def test_syo_maukkaasti_kateisella_alle_hinnan_antaa_oikeat_arvot(self) :
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(240)
        kassassa_rahaa = self.kassa.kassassa_rahaa
        maukkaat = self.kassa.maukkaat
        self.assertEqual((vaihtoraha, kassassa_rahaa, maukkaat), (240, 100_000, 0))

    def test_syo_edullisesti_kortilla_antaa_oikeat_arvot(self) :
        onnistui = self.kassa.syo_edullisesti_kortilla(self.kortti)
        kortin_saldo = self.kortti.saldo
        edulliset = self.kassa.edulliset
        kassassa_rahaa = self.kassa.kassassa_rahaa
        self.assertEqual((onnistui, kortin_saldo, edulliset, kassassa_rahaa), (True, 760, 1, 100_000))
    
    def test_syo_edullisesti_kortilla_antaa_oikeat_arvot_kun_saldo_ei_riita(self) :
        self.kortti.ota_rahaa(800)
        onnistui = self.kassa.syo_edullisesti_kortilla(self.kortti)
        kortin_saldo = self.kortti.saldo
        edulliset = self.kassa.edulliset
        self.assertEqual((onnistui, kortin_saldo, edulliset), (False, 200, 0))
    
    def test_syo_maukkaasti_kortilla_antaa_oikeat_arvot(self) :
        onnistui = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        kortin_saldo = self.kortti.saldo
        maukkaat = self.kassa.maukkaat
        kassassa_rahaa = self.kassa.kassassa_rahaa
        self.assertEqual((onnistui, kortin_saldo, maukkaat, kassassa_rahaa), (True, 600, 1, 100_000))
    
    def test_syo_maukkaasti_kortilla_antaa_oikeat_arvot_kun_saldo_ei_riita(self) :
        self.kortti.ota_rahaa(700)
        onnistui = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        kortin_saldo = self.kortti.saldo
        maukkaat = self.kassa.maukkaat
        self.assertEqual((onnistui, kortin_saldo, maukkaat), (False, 300, 0))
  
    def test_lataa_rahaa_lisaa_kassaan_ja_kortille(self) :
        self.kassa.lataa_rahaa_kortille(self.kortti, 500)
        kassassa_rahaa = self.kassa.kassassa_rahaa
        kortin_saldo = self.kortti.saldo
        self.assertEqual((kassassa_rahaa, kortin_saldo), (100_500, 1500))
    
    def test_negatiivisella_summalla_ei_voi_lataa_kortille(self) :
        self.kassa.lataa_rahaa_kortille(self.kortti, -300)
        kassassa_rahaa = self.kassa.kassassa_rahaa
        self.assertEqual(kassassa_rahaa, 100_000)