# 1431. Kids With the Greatest Number of Candies
# There are n kids with candies. You are given an integer array candies, where each candies[i] represents 
# the number of candies the ith kid has, and an integer extraCandies, 
# denoting the number of extra candies that you have.
# Return a boolean array result of length n, where result[i] is true if, after giving the 
# ith kid all the extraCandies, they will have the greatest 
# number of candies among all the kids, or false otherwise.
# Note that multiple kids can have the greatest number of candies.

from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    highest = candies[0]
    array_boolean = [0] * len(candies)

    for i in range(1, len(candies)):
        if candies[i] > highest:
            highest = candies[i]
    
    for i in range(len(candies)):
        if candies[i] + extraCandies >= highest:
            array_boolean[i] = True
        else:
            array_boolean[i] = False
    
    return array_boolean


candies = [12,1,12]
extraCandies = 10
print(kidsWithCandies(candies, extraCandies))