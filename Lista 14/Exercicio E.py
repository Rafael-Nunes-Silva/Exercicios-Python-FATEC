# H. not_bad
# Dada uma string, procura a primeira ocorrência de 'not' e 'bad'
# Se 'bad' aparece depois de 'not' troca 'not' ... 'bad' por 'good'
# Assim 'This dinner is not that bad!' retorna 'This dinner is good!'
def not_bad(s):
    notPos = s.find("not")
    badPos = s.find("bad")
    if badPos > notPos:
        return s[:notPos] + "good" + s[badPos+3:]
    return s