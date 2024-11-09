# 42. Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

from typing import List

def trap(height: List[int]) -> int:
    teste = 6

    for i in range(len(height)):
        teste += i

    return i



height = [4,2,2,5]
print(trap(height))