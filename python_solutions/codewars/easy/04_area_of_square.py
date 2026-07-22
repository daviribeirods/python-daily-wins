from math import pi, pow

# Problema: queremos descobrir a área do quadrado da figura com base no arco dado a seguir.
# Observações: Se imaginarmos o restante da figura, o arco é parte de um círculo maior,
# e o raio deste círculo é igual ao tamanho do lado do retângulo. Logo, se encontrarmos o raio,
# acharemos também o lado do quadrado, podendo então calcular a área do quadrado.

# A circunferência de um círculo é dada pela fórmula:
# C = 2 * pi * raio
# Logo, como temos o arco, que é 1/4 da circunferência, temos:
# Arco = (2 * pi * raio ) / 4
# Fazendo as reduções e isolando o raio, temos que o raio é:
# raio = (2 * arco) / pi
# logo, a área do quadrado é dada por:
# raio² = área do quadrado = [(2 * arco) / pi]²
def square_area(a):
    return pow((2*a)/pi,2)