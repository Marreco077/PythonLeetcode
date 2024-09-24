# Given two strings s and t, return true if the two strings 
# are anagrams of each other, otherwise return false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t