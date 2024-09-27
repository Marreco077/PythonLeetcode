# Given an integer num, return the number of digits in num that divide num.

# An integer val divides nums if nums % val == 0.

def countDigits(num: int) -> int:
    
    count = 0
    original_num = num

    if num < 10:
        return 1
        
    while num > 0:
        digit = num % 10
        if digit != 0 and original_num % digit == 0:
            count += 1
        num //= 10

    return count

num = 100
print(countDigits(num))