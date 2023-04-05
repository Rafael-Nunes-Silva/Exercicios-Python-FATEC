a = int(input("Insira o primeiro número: "))
b = int(input("Insira o segundo número: "))

maior = max(a, b)
menor = min(a, b)

while maior != menor:
    tmpMaior = maior - menor
    maior = max(tmpMaior, menor)
    menor = min(tmpMaior, menor)

print(f"O máximo divisor comum entre {a} e {b} é {maior}")
