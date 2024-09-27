# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

def checkIfPangram(sentence: str) -> bool:
    result = set(sentence)

    if len(result) == 26:
        return True
    return False
    
    



sentence = "thequickbrownfoxjumpsoverthelazydogqwqwqwqw"
print(checkIfPangram(sentence))