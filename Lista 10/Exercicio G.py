# G. count_code #
# conta quantas vezes aparece 'code'
# a letra 'd' pode ser trocada por outra qualquer
# assim 'coxe' ou 'coze' também são contadas como 'code'
# count_code('aaacodebbb') -> 1
# count_code('codexxcode') -> 2
# count_code('cozexxcope') -> 2
# cozexxcope
def count_code(s):
    cnt = 0
    for i in range(0, len(s)):
        if is_code(s[i:i+4]):
           cnt += 1
           i += 4
    return cnt

def is_code(s):
    if len(s) < 4:
        return False
    return True if s[0:2] == "co" and s[-1] == "e" else False
