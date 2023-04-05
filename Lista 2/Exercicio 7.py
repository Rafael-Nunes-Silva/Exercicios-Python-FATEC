areaPintada = float(input("Informe o tamanho da área a ser pintada (m²): "))

latas = int(areaPintada/54)

if areaPintada % 54 > 0:
    latas += 1

print(f"Serão necessárias {latas} latas de tinta que custarão {latas * 80} reais")
