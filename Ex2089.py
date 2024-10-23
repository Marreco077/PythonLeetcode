# 2089. Find Target Indices After Sorting Array
# You are given a 0-indexed integer array nums and a target element target.
# A target index is an index i such that nums[i] == target.
# Return a list of the target indices of nums after sorting nums in non-decreasing order.
# If there are no target indices, return an empty list.
# The returned list must be sorted in increasing order.

from typing import List

def targetIndices(nums: List[int], target: int) -> List[int]:
    new_arr = []
    arr_index = []

    while len(nums) > 0:
        low = nums[0]
        low_index = 0


        for i in range(1, len(nums)):
            if nums[i] < low:
                low = nums[i]
                low_index = i

        new_arr.append(nums.pop(low_index))

    for i in range(len(new_arr)):
        if new_arr[i] == target:
            arr_index.append(i)
            
    return arr_index

nums = [1,2,5,2,3]
target = 3

print(targetIndices(nums, target))