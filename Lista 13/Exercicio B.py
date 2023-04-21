# B. x_antes
# Dada uma lista de strings retorna uma lista onde
# todos os elementos que começam com x ficam sorteados antes 
# Ex.: ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] retorna
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Dica: monte duas listas separadas e junte-as no final
def x_antes(words):
    comX, semX = [], []
    for s in words:
        if s[0] == 'x':
            comX.append(s)
        else: semX.append(s)
    return sorted(comX) + sorted(semX)