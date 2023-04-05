# B. lone_sum
# Soma maluca: some os números inteiros a, b, e c
# Se algum número aparecer repetido ele não conta na soma
# lone_sum(1, 2, 3) -> 6
# lone_sum(3, 2, 3) -> 2
# lone_sum(3, 3, 3) -> 0
def lone_sum(a, b, c):
    res = 0
    if a != b and a != c:
        res += a
    if b != a and b != c:
        res += b
    if c != a and c != b:
        res += c
    return res
