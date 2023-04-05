# I. troca
# seja uma string s
# se s tiver tamanho <= 1 retorna ela mesma
# caso contrário troca a primeira e última letra
# troca('code') -> 'eodc'
# troca('a') -> 'a'
# troca('ab') -> 'ba'
def troca(s):
  if len(s) <= 1:
    return s
  tmp = list(s)
  tmp[0], tmp[-1] = tmp[-1], tmp[0]
  return "".join(tmp)
