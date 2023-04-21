# L. inicio em potencia de 2
# Dado um número inteiro positivo n retorne a primeira potência de 2
# que tenha o início igual a n
# Exemplo: para n = 65 retornará 16 pois 2**16 = 65536
def inip2(n):
    n = str(n)
    i = 2
    while str(pow(2, i))[:len(n)] != n:
        i += 1
    return i