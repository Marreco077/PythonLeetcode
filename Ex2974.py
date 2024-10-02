# 2974. Minimum Number Game
# You are given a 0-indexed integer array nums of even length and there is 
#  an empty array arr. Alice and Bob decided to play a game where in every round Alice and Bob will do one move. The rules of the game are as follows:
# Every round, first Alice will remove the minimum element from nums, and then Bob does the same.
# Now, first Bob will append the removed element in the array arr, and then Alice does the same.
# The game continues until nums becomes empty.
# Return the resulting array arr.

from typing import List

def numberGame(nums: List[int]) -> List[int]:
    result = []
    nums.sort()

    while len(nums) > 0:
        alice_pick = nums.pop(0)
        bob_pick = nums.pop(0)

        result.append(bob_pick)
        result.append(alice_pick)

    return result

nums = [5,4,2,3]
print(numberGame(nums))