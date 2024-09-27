# 2535. Difference Between Element Sum and Digit Sum of an Array
# You are given a positive integer array nums.

# The element sum is the sum of all the elements in nums.
# The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.

# Note that the absolute difference between two integers x and y is defined as |x - y|.

from typing import List

def differenceOfSum(nums: List[int]) -> int:
    sum_total = 0
    digit_sum = 0

    for num in nums:
        sum_total += num
        while num > 0:
            digit_sum += num % 10
            num //= 10
       

    diff = sum_total - digit_sum
    return diff

nums = [12,97,48,72,31,70,14,78]
print(differenceOfSum(nums))