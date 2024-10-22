# 35. Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    lower = 0 
    higher = len(nums) - 1

    while lower <= higher:
        mid = (lower + higher) // 2
        guess = nums[mid]

        if guess == target:
            return mid
        if guess < target:
            lower = mid + 1
        else:
            higher = mid - 1

    return lower
    
nums = [-1,3,5,6]
target = 0
print(searchInsert(nums, target))
