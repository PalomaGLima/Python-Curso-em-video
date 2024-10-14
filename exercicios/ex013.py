import math

# Entrada: lê o valor do ângulo em graus
angulo = float(input("Digite o ângulo em graus: "))

# Conversão de graus para radianos (as funções trigonométricas em Python usam radianos)
angulo_rad = math.radians(angulo)

# Cálculo do seno, cosseno e tangente
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

# Exibe os resultados
print(f"O seno de {angulo}° é: {seno:.4f}")
print(f"O cosseno de {angulo}° é: {cosseno:.4f}")
print(f"A tangente de {angulo}° é: {tangente:.4f}")