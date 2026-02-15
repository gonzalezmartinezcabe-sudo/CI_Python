"""
Tests para el módulo calculadora
"""

import unittest
import sys
import os

# Añadir el directorio src al path para importar
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):
    """Tests para la clase Calculadora"""

    def setUp(self):
        """Se ejecuta antes de cada test"""
        self.calc = Calculadora()

    def test_sumar(self):
        """Test de la suma"""
        self.assertEqual(self.calc.sumar(2, 3), 5)
        self.assertEqual(self.calc.sumar(-1, 1), 0)
        self.assertEqual(self.calc.sumar(0, 0), 0)

    def test_restar(self):
        """Test de la resta"""
        self.assertEqual(self.calc.restar(5, 3), 2)
        self.assertEqual(self.calc.restar(0, 5), -5)

    def test_multiplicar(self):
        """Test de la multiplicación"""
        self.assertEqual(self.calc.multiplicar(3, 4), 12)
        self.assertEqual(self.calc.multiplicar(-2, 3), -6)
        self.assertEqual(self.calc.multiplicar(0, 100), 0)

    def test_dividir(self):
        """Test de la división"""
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertEqual(self.calc.dividir(7, 2), 3.5)

    def test_dividir_por_cero(self):
        """Test de división por cero - debe lanzar excepción"""
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

    def test_potencia(self):
        """Test de potencia"""
        self.assertEqual(self.calc.potencia(2, 3), 8)
        self.assertEqual(self.calc.potencia(5, 0), 1)
        self.assertEqual(self.calc.potencia(10, 2), 100)


if __name__ == '__main__':
    unittest.main()