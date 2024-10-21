# 137. Single Number II
# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
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

nums = [0,1,0,1,0,1,99]
print(singleNumber(nums))
