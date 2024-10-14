'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. calcule o preço a pagar, sabendo que o carro custa 60 por dia e 0,15 por km rodade.
'''

d = float (input('quantos dias '))
km = float (input('quantos km '))

pagard = d * 60
pagarkm = km * 0.15

pagart = pagard + pagarkm

print ('O total a pagar é de ', pagart)