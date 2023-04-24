#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Exercícios extras para listas

# D. Dada uma lista de números retorna uma lista sem os elementos repetidos
def remove_iguais(nums):
    ret = []
    for n in nums:
        if n not in ret:
            ret.append(n)
    return sorted(ret)

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

# F. Derivada de um polinômio
# Os coeficientes de um polinômio estão numa lista na ordem do seu grau.
# Você deverá devolver uma lista com os coeficientes da derivada.
# Exemplo: [3, 2, 5, 2] retorna [2, 10, 6]
# A derivada de 3 + 2x + 5x^2 + 2x^3 é 2 + 10x + 6x^2
def derivada(coef):
    deriv = []
    for i in range(1, len(coef)):
        deriv.append(int(coef[i]) * i)
    return deriv


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

# H. Anagrama
# Verifique se duas palavras são anagramas,
# isto é são uma é permutação das letras da outra
# anagrama('aberto', 'rebato') = True
# anagrama('amor', 'ramo') = True
# anagrama('aba', 'baba') = False
def anagrama(s1, s2):
    p1, p2 = [], []
    for c in s1:
        p1.append(c)
    for c in s2:
        p2.append(c)
    return sorted(p1) == sorted(p2)

def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
    print ('remove_iguais')
    test(remove_iguais([2, 2, 1, 3]), [1, 2, 3])
    test(remove_iguais([2, 2, 3, 2, 3]), [2, 3])
    test(remove_iguais([]), [])

    print ()
    print ('cripto')
    test(cripto('ana e mariana gostam de banana'),
             'an e aimnr agmost de abn')
    test(cripto('Batatinha quando nasce esparrama pelo chão'),
             'Bahint adnoqu acens aemprs elop choã')

    print ()
    print ('derivada de polinômio')
    test(derivada([3, 0, 4, 3, 5]), [0, 8, 9, 20])
    test(derivada([4, 16, 1]), [16, 2])

    print ()
    print ('soma em listas invertidas')
    test(soma([5, 2, 3, 4], [9, 8, 7, 8]), [4, 1, 1, 3, 1])
    test(soma([3, 1, 5], [5, 9, 2]), [8, 0, 8])

    print ()
    print ('anagrama')
    test(anagrama('sim', 'siiimmmmm'), False)
    test(anagrama('iracema', 'america'), True)
    test(anagrama('ator', 'rota'), True)
    test(anagrama('aberto', 'rebato'), True)
    test(anagrama('amor', 'roma'), True)
    test(anagrama('ramo', 'amor'), True)
    test(anagrama('baba', 'aba'), False)
    test(anagrama('casa', 'cassa'), False)
    test(anagrama('palmeiras', 'abacate'), False)


if __name__ == '__main__':
    main()