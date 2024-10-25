# 1732. Find the Highest Altitude
# There is a biker going on a road trip. The road trip consists of n + 1
# points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
# You are given an integer array gain of length n where gain[i] is 
# the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

from typing import List

def largestAltitude(gain: List[int]) -> int:
    highest = 0
    sum_all = 0

    for altitude in gain:
        sum_all += altitude
        
        if sum_all > highest:
            highest = sum_all

    return highest

gain = [-4,-3,-2,-1,4,3,2]
print(largestAltitude(gain))