
"""
faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pintá-la, sabendo que cada litro de tinta, pinta uma area de 2m2.
"""

L = float (input('digite a largura da parede: '))
H = float (input('digite a altura da parede: '))

Ap = L * H

T = Ap/2

print ('a quantidade de tinta necessaria e', T)
