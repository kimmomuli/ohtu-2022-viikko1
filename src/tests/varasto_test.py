import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.virheellinen_varasto = Varasto(-10, -1)
        self.valmiiksi_taysi_varasto = Varasto(5, 10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        #self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto.saldo, 1230)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_likaa_tavaraa_varastoon(self):
        self.varasto.lisaa_varastoon(15)

        self.assertEqual('saldo = 10, vielä tilaa 0', str(self.varasto))

    def test_ota_varastosta_negatiivine(self):
        self.varasto.ota_varastosta(-1)
        self.assertEqual('saldo = 0, vielä tilaa 10', str(self.varasto))

    def test_lisaa_varastoon_negatiivine(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertEqual('saldo = 0, vielä tilaa 10', str(self.varasto))

    def test_ota_varastosta_liikaa(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(10)
        self.assertEqual('saldo = 0.0, vielä tilaa 10.0', str(self.varasto))

    def test_virheellinen_varasto(self):
        self.assertEqual('saldo = 0.0, vielä tilaa 0.0', str(self.virheellinen_varasto))

    def test_luoda_liian_taysi_varasto(self):
        self.assertEqual('saldo = 5, vielä tilaa 0', str(self.valmiiksi_taysi_varasto))

