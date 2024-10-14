#crie um algoritmo que leia um numero e mostre seu dobro, seu triplo e sua raiz quadrada


n = int (input('digite um numero'))

dobro = n*2
triplo = n*3
raiz = n**(1/2)

print('o dobro de {} vale {}.'.format(n,dobro))
print('o triplo de {} vale {}. A raiz quadrada de {} é igual a {}'.format(n,triplo,n,raiz))