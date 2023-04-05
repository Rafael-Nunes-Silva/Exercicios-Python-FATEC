valor = float(input("Insira o preço da mercadoria: "))
desconto = float(input("Insira o valor percentual de desconto: "))

print("O valor com o desconto é ", valor * (1 - desconto/100))
