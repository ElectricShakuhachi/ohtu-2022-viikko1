import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    #KONSTRUKTORIIN LIITTYVÄT TESTIT:
    def test_konstruktori_luo_tyhjan_varaston(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_voidaan_luoda_saldolla(self):
        self.varasto = Varasto(10, 8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_negatiivisella_saldolla_luodun_varaston_saldo_nolla(self):
        self.varasto = Varasto(10, -10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivisella_tilavuudella_luodun_varaston_tilavuus_nolla(self):
        self.varasto = Varasto(-10)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_tilavuutta_isompi_saldo_luodessa_vähentyy_tilavuuden_mukaan(self):
        self.varasto = Varasto(10, 20)
        self.assertAlmostEqual(self.varasto.tilavuus, self.varasto.saldo)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    #paljonko_mahtuu LIITTYVÄT TESTIT:
    def test_paljonko_mahtuu_palauttaa_tilavuuden_ja_saldon_erotuksen(self):
        self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 5)

    #lisaa_varastoon LIITTYVÄT TESTIT:
    def test_lisays_negatiivisella_arvolla_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_saldon_lisays_yli_tilavuuden_nostaa_saldon_maksimiin(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    #ota_varastosta LIITTYVÄT TESTIT:
    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivinen_otto_palauttaa_nollan(self):
        saatu_maara = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_yli_saldon_ottaminen_palauttaa_saldon_verran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(12)
        self.assertAlmostEqual(saatu_maara, 8)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_class_string_returns_a_string(self):
        self.assertIsInstance(str(self.varasto), str)