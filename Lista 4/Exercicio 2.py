import random

numeros = random.sample(range(1, 101), 20)
impares, pares = [], []

for x in numeros:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

print(f"Números sorteados: {numeros}\nNúmeros pares: {pares}\nNúmeros impares: {impares}")
