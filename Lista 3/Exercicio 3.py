cidadeA = 80000
cidadeB = 200000

a = cidadeA
b = cidadeB

cnt = 0

while a < b:
    a *= 1.03
    b *= 1.015
    cnt += 1

print(f"Serão necessários {cnt} anos para que a população A seja igual ou maior que a B")
