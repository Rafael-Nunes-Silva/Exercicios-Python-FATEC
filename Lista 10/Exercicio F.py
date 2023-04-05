# F. cat_dog #
# verifica se o aparece o mesmo número de vezes 'cat' e 'dog'
# cat_dog('catdog') -> True
# cat_dog('catcat') -> False
# cat_dog('1cat1cadodog') -> True
def cat_dog(s):
    catCnt, dogCnt = 0, 0
    for i in range(0, len(s)):
        if s[i:i+3] == "cat":
           catCnt += 1
           i += 2

    for i in range(0, len(s)):
        if s[i:i+3] == "dog":
           dogCnt += 1
           i += 2
    return True if catCnt == dogCnt else False
