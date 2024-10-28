# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    hashmap = {}

    for numbers in nums:
        if numbers in hashmap:
            hashmap[numbers] += 1
        else:
            hashmap[numbers] = 1

    return list(hashmap.keys())
    print(teste)

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
