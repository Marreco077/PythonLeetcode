# 3024. Type of Triangle
# ou are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

# A triangle is called equilateral if it has all sides of equal length.
# A triangle is called isosceles if it has exactly two sides of equal length.
# A triangle is called scalene if all its sides are of different lengths.
# Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

from typing import List

def triangleType(self, nums: List[int]) -> str:

    if nums[0] >= nums[1] + nums[2] or nums[1] >= nums[0] + nums[2] or nums[2] >= nums[0] + nums[1]:
        return "none"

    side1 = nums[0]
    side2 = nums[1]
    side3 = nums[2]

    if side1 == side2 and side1 == side3:
        return "equilateral"
    
    elif side1 == side2 or side1 == side3 or side2 == side3: 
        return "isosceles"
    
    else:
        return "scalene"

nums = [3, 3, 3]
