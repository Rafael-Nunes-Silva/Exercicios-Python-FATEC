# D. Dada uma lista de números retorna uma lista sem os elementos repetidos
def remove_iguais(nums):
    ret = []
    for n in nums:
        if n not in ret:
            ret.append(n)
    return sorted(ret)