import random

lista = random.sample(range(1, 101), 10)
menor, maior = 100, 0

for x in lista:
    if x < menor:
        menor = x
    if x > maior:
        maior = x

print(f"O menor e maior número da lista:\n{lista}\nsão respectivamente: {menor}, {maior}")
