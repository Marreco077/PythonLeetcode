# 383. Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    hashmap_ransom = {}
    hashmap_magazine = {}

    for letter in ransomNote:
        if letter in hashmap_ransom:
            hashmap_ransom[letter] += 1
        else:
            hashmap_ransom[letter] = 1
        
    for letter in magazine:
        if letter in hashmap_magazine:
            hashmap_magazine[letter] += 1
        else:
            hashmap_magazine[letter] = 1
        
    for letter in hashmap_ransom:
        if hashmap_ransom[letter] > hashmap_magazine.get(letter, 0):
            return False
            
    return True

ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
print(canConstruct(ransomNote, magazine))
