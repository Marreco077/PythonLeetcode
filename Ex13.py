# 13. Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 
# 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.


def romanToInt(s: str) -> int:
    dict_romans = {"I": 1, "V": 5, "X": 10,
                   "L": 50, "C": 100, "D": 500,
                   "M": 1000}
    
    count = 0
    prev_value = 0

    for i in range(len(s)-1,-1,-1):
        current_value = dict_romans[s[i]]

        if current_value < prev_value:
            count -= current_value
        else:
            count += current_value
        
        prev_value = current_value

    return count

s = "MMMCDXC"
print(romanToInt(s))