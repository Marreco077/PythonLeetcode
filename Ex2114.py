# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

# You are given an array of strings sentences, where each sentences[i] represents a single sentence.

# Return the maximum number of words that appear in a single sentence.

from typing import List

def mostWordsFound(sentences: List[str]) -> int:
    max_words = 0

    for sentence in sentences:
        word_count = len(sentence.split())

        max_words = max(max_words, word_count)

    return max_words

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(mostWordsFound(sentences))