# 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

from typing import List

def singleNumber(nums: List[int]) -> int:
    hashmap = {}

    for numbers in nums:
        if numbers in hashmap:
            hashmap[numbers] += 1
        else:
            hashmap[numbers] = 1


    for number, count in hashmap.items():
        if count == 1:
            return number

nums = [4,1,2,1,2]
print(singleNumber(nums))
