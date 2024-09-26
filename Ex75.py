# Given an array nums with n objects colored red, white, or blue, 
# sort them in-place so that objects of the same color are adjacent, 
# with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

from typing import List

def sortColors(nums: List[int]) -> None:
    count0, count1, count2 = 0, 0, 0

    for num in nums:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1

    for i in range(len(nums)):
        if i < count0:
            nums[i] = 0
        elif i < count0 + count1:
            nums[i] = 1
        else:
            nums[i] = 2
    print(nums)

nums = [2,0,2,1,1,0]   
sortColors(nums)