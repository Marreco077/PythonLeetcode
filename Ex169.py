# 169. Majority Element
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋
# times. You may assume that the majority element always exists in the array.

from typing import List


def majorityElement(nums: List[int]) -> int:
    hashmap = {}
    major = len(nums) / 2

    for i, num in enumerate(nums):
        if num not in hashmap:
            hashmap[num] = 1
        else:
            hashmap[num] += 1
        if hashmap[num] >= major:
            return num





nums = [3,2,3,2,2]
print(majorityElement(nums))