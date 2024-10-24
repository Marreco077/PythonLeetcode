# 485. Max Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

from typing import List

def findMaxConsecutiveOnes(nums: List[int]) -> int:
    if 1 not in nums:
        return 0

    count = [1] * len(nums)
    index = 0
    

    for i in range(len(nums) - 1):
        if nums[i] == 1:
            if nums[i+1] == nums[i]:
                count[index] += 1
            else:
                index += 1
    
    higher = 0

    for i in range(len(count)):
        if count[i] > higher:
            higher = count[i]

    return higher

nums = [0]
print(findMaxConsecutiveOnes(nums))