# 2652. Sum Multiples
# Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.

# Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

def sumOfMultiples(n: int) -> int:
    count = 0

    while n > 0:
        if n % 3 == 0 or n % 5 == 0 or n % 7 == 0: # all numbers divisible by 6 also divisible by 3
            count += n
        n -= 1
    return count

n = 9
print(sumOfMultiples(n))
