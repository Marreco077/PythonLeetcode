# Given two integers, num and t. A number is achievable if it can become equal to num after applying the following operation:

# Increase or decrease the number by 1, and simultaneously increase or decrease num by 1.
# Return the maximum achievable number after applying the operation at most t times.

def theMaximumAchievableX(num: int, t: int) -> int:
    test = t * 2

    return num + test



num, t = 3, 2
print(theMaximumAchievableX(num, t))