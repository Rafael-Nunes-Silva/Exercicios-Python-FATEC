# C. common_end #
# Dada duas listas a e b verifica se os dois primeiros são
# iguais ou os dois últimos são iguais
# suponha que as listas tenham pelo menos um elemento
# common_end([1, 2, 3], [7, 3]) -> True
# common_end([1, 2, 3], [7, 3, 2]) -> False
# common_end([1, 2, 3], [1, 3]) -> True
def common_end(a, b):
    return True if a[0] == b[0] or a[-1] == b[-1] else False
