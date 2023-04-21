# A. fim_igual
# Dada uma lista de strings, retorna o número de strings
# com tamanho >= 2 onde o primeiro e o último caracteres são iguais
# Exemplo: ['aba', 'xyz', 'aa', 'x', 'bbb'] retorna 3
def fim_igual(words):
    count = 0
    for s in words:
        if len(s) < 2:
            continue
        if s[0] == s[-1]:
            count += 1
    return count