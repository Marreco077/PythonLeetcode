# 977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order..

from typing import List



def sortedSquares(nums: List[int]) -> List[int]:
    for i, num in enumerate(nums):
        nums[i] = num ** 2
    nums.sort()
    return nums


nums = [-4,-1,0,3,10]
print(sortedSquares(nums))