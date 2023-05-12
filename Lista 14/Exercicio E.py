# E. Cripto desafio!!
# Dada uma frase, você deve retirar todas as letras repetidas das palavras
# e ordenar as letras que sobraram
# Exemplo: 'ana e mariana gostam de banana' vira 'an e aimnr agmost de abn'
# Dicas: tente transformar cada palavra em um conjunto,
# depois tente ordenar as letras e montar uma string com o resultado.
# Utilize listas auxiliares se facilitar
def cripto(frase):
    novaFrase = []
    for palavra in frase.split(" "):
        novaPalavra = ""
        for letra in palavra:
            if letra not in novaPalavra:
                novaPalavra += letra
        novaFrase.append("".join(sorted(novaPalavra)))
    return " ".join(novaFrase)