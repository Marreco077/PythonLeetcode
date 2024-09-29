# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List

def productExpectSelf(nums: List[int]) -> List[int]:
    product = 1
    test = 0
    answer = []

    for i in range(len(nums)):
        




nums = [1, 2, 3, 4]
print(productExpectSelf(nums))