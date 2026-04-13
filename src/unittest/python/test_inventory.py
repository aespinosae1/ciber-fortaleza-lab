import unittest
from inventory import VaccineManager
from validator import check_temp

class TestBioGuard(unittest.TestCase):
    def setUp(self):
        self.vm = VaccineManager()

    def test_stock_incremental(self):
        # Prueba la suma correcta de dosis
        self.vm.add_doses("Moderna", 100)
        self.vm.add_doses("Moderna", 50)
        self.assertEqual(self.vm.stock["Moderna"], 150)

    def test_exception_negative_qty(self):
        # Validación de seguridad ante datos negativos
        with self.assertRaises(ValueError):
            self.vm.add_doses("Error_Vial", -1)

    def test_range_temperature(self):
        # Validación de límites térmicos (-10 a 8)
        self.assertTrue(check_temp(0))   # Caso dentro del rango
        self.assertFalse(check_temp(30))  # Caso por encima
        self.assertFalse(check_temp(-20)) # Caso por debajo