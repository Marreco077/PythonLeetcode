# # 9. Palindrome Number
# Given an integer x, return true if x is a 
# palindrome, and false otherwise.

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    contrary = str(x)
    reverse_num = int(contrary[::-1])

    if x == reverse_num:
        return True
    else:
        return False


x = 121
print(isPalindrome(x))