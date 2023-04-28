# F. busca
# Verifique quantas ocorrências de uma palavra há numa frase
# frase = 'ana e mariana gostam de banana'
# palavra = 'ana'
# busca ('ana e mariana gostam de banana', 'ana') == 4
def busca(frase, palavra):
    count = 0
    for i in range(0, len(frase)-2):
        if frase[i:i+3] == palavra:
            count += 1
    return count