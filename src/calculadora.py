"""
Módulo de calculadora simple para demostrar CI/CD
"""


class Calculadora:
    """Calculadora con operaciones básicas"""

    def sumar(self, a, b):
        """
        Suma dos números

        Args:
            a (int/float): Primer número
            b (int/float): Segundo número

        Returns:
            int/float: Resultado de la suma
        """
        return a + b

    def restar(self, a, b):
        """Resta dos números"""
        return a - b

    def multiplicar(self, a, b):
        """Multiplica dos números"""
        return a * b

    def dividir(self, a, b):
        """
        Divide dos números

        Raises:
            ValueError: Si el divisor es cero
        """
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

    def potencia(self, base, exponente):
        """Calcula la potencia de un número"""
        return base ** exponente