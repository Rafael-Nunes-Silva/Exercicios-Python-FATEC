# K. has22 #
# Verifica se na lista de números inteiros aparecem dois 2 consecutivos
# has22([1, 2, 2]) -> True
# has22([1, 2, 1, 2]) -> False
# has22([2, 1, 2]) -> False
def has22(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False
