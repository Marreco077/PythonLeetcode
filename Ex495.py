# 495. Teemo Attacking
# Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, 
# Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second
#  t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, 
# the timer for it is reset, and the poison effect will end duration seconds after the new attack.
# You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes 
# that Teemo attacks Ashe at second timeSeries[i], and an integer duration.
# Return the total number of seconds that Ashe is poisoned.

from typing import List

def findPoisonedDuration(timeSeries: List[int], duration: int) -> int:
    poisoned = 0
   
    for i in range(len(timeSeries) - 1):
        if timeSeries[i + 1] - timeSeries[i] < duration:
            poisoned += timeSeries[i + 1] - timeSeries[i]
        else:
            poisoned += duration
    
    poisoned += duration # last attack always add duration


    return poisoned

timeSeries = [1, 4]
duration = 2
print(findPoisonedDuration(timeSeries, duration))