# 724. Find Pivot Index
# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to 
# the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum 
# is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

from typing import List

def pivotIndex(nums: List[int]) -> int:
    sum_right = 0
    sum_left = 0
    lengh = len(nums)


    for num in nums:
        sum_right += num

    for i in range(lengh):
        sum_right -= nums[i] 

        if sum_left == sum_right:  
            return i  
        
        sum_left += nums[i]  
    
    return -1

nums = [1,-1,4]
print(pivotIndex(nums))

