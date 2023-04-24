# J. zeros finais
# Verifique quantos zeros há no final de um número inteiro positivo
# Exemplo: 10010 tem 1 zero no fim e 908007000 possui três
def zf(n):
    n = str(n)
    i = len(n)-1
    while n[i] == '0':
        i -= 1
    return len(n)-1-i