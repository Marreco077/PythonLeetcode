# 1281. Subtract the Product and Sum of Digits of an Integer
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

def subtractProductAndSum(n: int) -> int:
    string_num = str(n) 
    product = 1
    sum_digits = 0

    for nums in string_num:
        int(nums)
        product *= nums
        sum_digits += nums
    return product - sum_digits

n = 234
print(subtractProductAndSum(n))