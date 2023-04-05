n = int(input("Insira o número: "))

ePrimo = 1

c = 2
while c < n:
    if n % c == 0:
        ePrimo = 0
        break
    c += 1

if ePrimo:
    print(f"{n} é primo")
else:
    print(f"{n} não é primo")
