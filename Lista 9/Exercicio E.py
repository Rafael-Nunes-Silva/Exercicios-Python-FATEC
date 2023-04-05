# E. sum2 #
# Dada uma lista de inteiros de qualquer tamanho
# retorna a soma dos dois primeiros elementos
# se a lista tiver menos de dois elementos, soma o que for possível
def sum2(nums):
    numsSum = 0
    for i in range(0, min(2, len(nums))):
        numsSum += nums[i]
    return numsSum
