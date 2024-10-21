# 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

from typing import List

def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    
    soma = 0
    for number in nums:
        soma += number
    
    soma_total = 0

    while n > 0:
        soma_total += n
        n -= 1

    return soma_total - soma



nums = [0,1]
print(missingNumber(nums))