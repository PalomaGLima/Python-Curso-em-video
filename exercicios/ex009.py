"""
Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salario, com 15% de aumento.
"""

salario = float (input('digite seu salario'))
aumento = salario + (salario * 15/100)
print('o novo salrio é ', aumento)