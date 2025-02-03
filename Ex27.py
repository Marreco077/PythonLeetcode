# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to 
# val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
#  The remaining elements of nums are not important as well as the size of nums.
# Return k.

from typing import List

def removeElement(nums: List[int], val: int) -> int:
    left = 0
    right = len(nums) - 1
    k = 0

    while left <= right:
        if nums[right] == val:
            right -= 1
            continue

        if nums[left] == val:
            nums[left], nums[right] = nums[right], nums[left]
        
        left += 1
    
    
    for num in nums:
        if num != val:
            k += 1
        else:
            return k


nums = [4,2,0,2,2,1,4,4,1,4,3,2]
val = 4
print(removeElement(nums, val))
        


