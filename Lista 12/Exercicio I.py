# I. inicio_final
# Divida cada string em dois pedaços.
# Se a string tiver um número ímpar de caracteres
# o primeiro pedaço terá um caracter a mais,
# Exemplo: 'abcde', divide-se em 'abc' e 'de'.
# Dadas 2 strings, a e b, retorna a string
# a_inicio + b_inicio + a_final + b_final
import math
def inicio_final(a, b):
    return a[:math.ceil(len(a)/2)] + b[:math.ceil(len(b)/2)] + a[math.ceil(len(a)/2):] + b[math.ceil(len(b)/2):]