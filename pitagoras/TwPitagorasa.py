# Autor: Jakub Płoskonka
# 03.2025
# klasa TwPitagorasa dod, odej, mnoz, dziel

from fractions import Fraction

def sqrt(param):
    return param ** 0.5


class TwPitagorasa:

    def oblicz_c(self,a,b):
        suma_kwadratow = (a ** 2 ) + (b ** 2)
        pierwiastek = sqrt(suma_kwadratow)
        return Fraction(pierwiastek).limit_denominator()

        
        
# k = TwPitagorasa()
# print(Fraction(k.oblicz_c(3,4)))
