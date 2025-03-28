import unittest
from fractions import Fraction
from TwPitagorasa import TwPitagorasa, sqrt

class TestTwPitagorasa(unittest.TestCase):

    def setUp(self):
        self.k = TwPitagorasa()

    def test_przyklad_klasyczny(self):
        wynik = self.k.oblicz_c(3, 4)
        self.assertEqual(wynik, Fraction(5, 1))

    def test_ulamki(self):
        wynik = self.k.oblicz_c(Fraction(3,4), Fraction(4,7))
        # nie porównujemy bezpośrednio, bo pierwiastek z ułamków nie zawsze da ładny wynik
        oczekiwany = Fraction(sqrt((Fraction(3,4)**2 + Fraction(4,7)**2))).limit_denominator()
        self.assertEqual(wynik, oczekiwany)

    def test_zero(self):
        wynik = self.k.oblicz_c(0, 0)
        self.assertEqual(wynik, Fraction(0, 1))

if __name__ == '__main__':
    unittest.main()
