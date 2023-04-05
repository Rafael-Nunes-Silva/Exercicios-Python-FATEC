a = float(input("Insira o tamanho do lado A: "))
b = float(input("Insira o tamanho do lado B: "))
c = float(input("Insira o tamanho do lado C: "))

if a > abs(b-c) or b > abs(a-c) or c > abs(a-b): # a <= b+c and b <= a+c and c <= a+b:
    tri = "!!!ERRO!!!"
    if a == b == c:
        tri = "equilátero"
    elif a != b != c:
        tri = "escaleno"
    elif (a == b and b != c) or (a != b and b == c) or (a == c and a != b):
        tri = "isóceles"
    print(f"Esse é um triângulo {tri}")
else:
    print(f"Não é posivel montar um triângulo de lados {a}, {b}, {c}")
