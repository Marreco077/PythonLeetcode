# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

def firstUniqChar(s: str) -> int:
    hashmap = {}
  
    for character in s:
        if character in hashmap:
            hashmap[character] += 1
        else:
            hashmap[character] = 1
            
    for char in hashmap:
        if hashmap[char] == 1:
            return s.index(char)
    
    return -1   


s = "loveleetcode"
print(firstUniqChar(s))