# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(n: int) -> int:
    step1 = 1
    step2 = 2
    result = 1
    number_climbing = n

    for i in range(n):
        if number_climbing > 1:
            number_climbing += 2
        number_climbing -= 1
        


n = 2
print(climbStairs(n))