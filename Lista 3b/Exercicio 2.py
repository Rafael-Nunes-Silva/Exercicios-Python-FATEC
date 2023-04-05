conta = int(input("Insira o valor da conta: "))
pago = int(input("Insira o valor pago: "))

notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0

if pago > conta:
    troco = pago - conta
    while troco >= 50:
        troco -= 50
        notas50 += 1
    while troco >= 20:
        troco -= 20
        notas20 += 1
    while troco >= 10:
        troco -= 10
        notas10 += 1
    while troco >= 5:
        troco -= 5
        notas5 += 1
    while troco >= 2:
        troco -= 2
        notas2 += 1
    while troco >= 1:
        troco -= 1
        notas1 += 1
    msg = "O troco será dado em:\n"
    if notas50 == 1:
        msg += "1 nota de 50\n"
    elif notas50 > 1:
        msg += f"{notas50} notas de 50\n"
    if notas20 == 1:
        msg += "1 nota de 20\n"
    elif notas20 > 1:
        msg += f"{notas20} notas de 20\n"
    if notas10 == 1:
        msg += "1 nota de 10\n"
    elif notas10 > 1:
        msg += f"{notas10} notas de 10\n"
    if notas5 == 1:
        msg += "1 nota de 5\n"
    elif notas5 > 1:
        msg += f"{notas5} notas de 5\n"
    if notas2 == 1:
        msg += "1 nota de 2\n"
    elif notas2 > 1:
        msg += f"{notas2} notas de 2\n"
    if notas1 == 1:
        msg += "1 nota de 1"
    elif notas1 > 1:
        msg += f"{notas1} notas de 1"
    print(msg)
elif pago < conta:
    print(f"Faltam {conta-pago} para completar o valor")
elif pago == conta:
    print("O valor pago está correto")
