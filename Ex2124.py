# 2124. Check if All A's Appears Before All B's
# Given a string s consisting of only the characters 'a' and 'b',
# return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

def checkString(s: str) -> bool:
    for i in range(1, len(s)):
        if s[i-1] == "b" and s[i] == "a":
            return False
    
    return True

s = "abab"
print(checkString(s))