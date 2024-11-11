# # 9. Palindrome Number
# Given an integer x, return true if x is a 
# palindrome, and false otherwise.

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    
    contrary = str(x)
    
    l = 0
    r = len(contrary) - 1
    
    while l <= r:
        if contrary[l] != contrary[r]:
            return False
        l += 1
        r -= 1

    return True

x = 121
print(isPalindrome(x))