# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and r
# emoving all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.


def isPalindrome(s: str) -> bool:
    index = 0
    s = s.lower()

    while index < len(s):
        if s[index].isalnum() == False:
            s = s.replace(s[index], "", 1)
        else:
            index += 1
    
    
    left = 0
    right = len(s) - 1

    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


s = " "
print(isPalindrome(s))