# 345. Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they 
# can appear in both lower and upper cases, more than once.

def reverseVowels(s: str) -> str:
    # só colocar varios ifs alterando ascci maisculo/minusculo pelo contrario
    arr = [0] * len(s)
    
    for word in s:
        if word < 0:
            pass




s = "IceCreAm"
print(reverseVowels(s))