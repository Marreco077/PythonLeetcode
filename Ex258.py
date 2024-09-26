# 258. Add Digits
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

def addDigits(num:int ) -> int:
    while(num >= 9):
        num = (num // 10) + (num % 10) 
    return int(num)

num = 18
print(addDigits(num))