# 1281. Subtract the Product and Sum of Digits of an Integer
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

def subtractProductAndSum(n: int) -> int:
    product = 1
    sum_digits = 0

    while n > 0:
        product = (n % 10) * product
        sum_digits = (n % 10) + sum_digits
        n //= 10
    
    return product - sum_digits
        
        
    
    

n = 4421
print(subtractProductAndSum(n))