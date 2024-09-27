# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.

from typing import List

def firstPalindrome(words: List[str]) -> str:
    for word in words:
        if word[::-1] == word:
            return word
    return ""


words = ["def","ghi"]
print(firstPalindrome(words))