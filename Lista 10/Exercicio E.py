# E. count_hi #
# conta o número de vezes que aparece a string 'hi'
# count_hi('abc hi ho') -> 1
# count_hi('ABChi hi') -> 2
# count_hi('hihi') -> 2
def count_hi(s):
    cnt = 0
    for i in range(0, len(s)):
        if s[i:i+2] == "hi":
           cnt += 1
           i += 1
    return cnt
