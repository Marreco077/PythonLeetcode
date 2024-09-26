# Given an array of strings strs, group the anagrams
# together. You can return the answer in any order.
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    hashmap = {} 

    for i, n in enumerate(str):
        hashmap[n] = i
    
    for i in range(hashmap):
        

lista = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(lista))