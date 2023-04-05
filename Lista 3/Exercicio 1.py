n = int(input("Insira uma nota entre 0 e 10: "))

while n < 0 or n > 10:
    n = int(input("Insira uma nota válida: "))

print("Valor válido inserido")
