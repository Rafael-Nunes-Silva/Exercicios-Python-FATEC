# D. mistura2
# Sejam duas strings a e b
# Retorno uma string '<a> <b>' separada por um espaço
# com as duas primeiras letras trocadas de cada string 
#     'mix', pod' -> 'pox mid'
#     'dog', 'dinner' -> 'dig donner'
def mistura2(a, b):
    return f"{b[:2] + a[2:]} {a[:2] + b[2:]}"