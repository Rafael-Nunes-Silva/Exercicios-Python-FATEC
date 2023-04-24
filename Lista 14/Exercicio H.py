# K. conta 2
# Verifique quantas vezes o dígito 2 aparece entre 0 e n-1
# Exemplo: para n = 20 o dígito 2 aparece duas vezes entre 0 e 19
def conta2(n):
    count = 0
    for i in range(0, n):
        count += str(i).count("2")
    return count