"""
Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros.
"""

n = float (input ('digite o valor'))

cm = n * 100
mm = n * 1000

print ('a medida de {}m corresponde a  {}cm e {}mm'.format(n,cm,mm))