import random

vet1, vet2 = random.sample(range(1, 101), 10), random.sample(range(1, 101), 10)
intercalado = []

for x in range(0, 10):    
    intercalado.append(vet1[x])
    intercalado.append(vet2[x])

print(f"Vetor1: {vet1}\nVetor2: {vet2}\nIntercalado: {intercalado}")
