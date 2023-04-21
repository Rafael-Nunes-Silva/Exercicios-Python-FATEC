# E. palindrome
# Verifique se uma string é palíndrome
#     palindrome('asa') True
#     palindrome('casa') False 
def palindrome(s):
    return s == s[::-1]