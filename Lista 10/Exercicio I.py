# I. count_evens
# conta os números pares da lista
# count_evens([2, 1, 2, 3, 4]) -> 3
# count_evens([2, 2, 0]) -> 3
# count_evens([1, 3, 5]) -> 0
def count_evens(nums):
    cnt = 0
    for n in nums:
        if n % 2 == 0:
            cnt += 1
    return cnt
