# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, 
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

from typing import List

def search(nums: List[int], target: int) -> int:
    lower = 0
    higher = len(nums) - 1

    while lower <= higher:
        mid = (higher + lower) // 2
        guess = nums[mid]

        if guess == target:
            return mid
        if guess > target:
            higher = mid - 1
        else:
            lower = mid + 1

    return -1


nums = [-1,0,3,5,9,12]
target = 2
print(search(nums, target))