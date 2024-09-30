# 709. To Lower Case
# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

def toLowerCase(s: str) -> str:
   concatenated = ""
   
   for char in s:
      if 'A' <= char <= 'Z':
         concatenated += chr(ord(char) + 32)
      else:
         concatenated += char

   return concatenated

s = "LOVELY"
print(toLowerCase(s))