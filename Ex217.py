#  217. Contains Duplicate
#     Given an integer array nums, return true if any value appears at 
# least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()

        for numbers in nums:
            my_set.add(numbers)

        if len(my_set) != len(nums):
            return True
        
        else: 
            return False