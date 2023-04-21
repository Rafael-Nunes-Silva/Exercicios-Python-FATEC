# G. verbing
# Dada uma string, caso seu comprimento seja pelo menos 3,
# adiciona 'ing' no final
# Caso a string já termine em 'ing', acrescentará 'ly'.
def verbing(s):
    if len(s) < 3:
        return s
    return s + ("ly" if s[-3:] == "ing" else "ing")