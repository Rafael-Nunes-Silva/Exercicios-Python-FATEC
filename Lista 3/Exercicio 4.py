pos = int(input("Insira a posição: "))

prev, at = 0, 1

c = 1
while c < pos:
    prev, at = at, prev+at
    c += 1

print(f"O número da sequência de Fibonacci na posição {pos} é {at}")
