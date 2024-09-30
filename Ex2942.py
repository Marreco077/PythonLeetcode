# 2942. Find Words Containing Character
# You are given a 0-indexed array of strings words and a character x.

# Return an array of indices representing the words that contain the character x.

# Note that the returned array may be in any order.

from typing import List


def findWordsContaining(words: List[str], x: str) -> List[int]:
    result = []


    for i, word in enumerate(words):
        if x in word:
            result.append(i)

    return result


words = ["abc","bcd","aaaa","cbc"]
x = "q"
print(findWordsContaining(words, x))