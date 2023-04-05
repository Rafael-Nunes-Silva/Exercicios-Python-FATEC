# B. string_splosion
# string_splosion('Code') -> 'CCoCodCode'
# string_splosion('abc') -> 'aababc'
# string_splosion('ab') -> 'aab'
def string_splosion(s):
    res = ""
    for i in range(1, len(s)+1):
        res += s[0:i]
    return res
