kgPescado = int(input("Insira a quantidade de peixes pescados em kilo: "))

if kgPescado > 50:
    print(f"Haverá uma multa de {4*(kgPescado-50)} reais")
else:
    print("Não haverá multa")
