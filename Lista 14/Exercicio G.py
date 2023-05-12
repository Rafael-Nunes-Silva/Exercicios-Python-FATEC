# G. Soma em listas invertidas
# Colocamos os dígitos de dois números em listas ao contrário
# 513 vira [3, 1, 5] e 295 vira [5, 9, 2]
# [3, 1, 5] + [5, 9, 2] = [8, 0, 8]
# pode supor que n1 e n2 tem o mesmo número de dígitos
# Não vale converter a lista em número para somar diretamente
def soma(n1, n2):
    soma = []
    for i in range(0, len(n1)):
        soma.append(int(n1[i]) + int(n2[i]))
    for i in range(0, len(soma)):
        if soma[i] >= 10:
            soma[i] -= 10
            if i == len(soma)-1:
                soma.append(1)
            else: soma[i+1] += 1
    return soma