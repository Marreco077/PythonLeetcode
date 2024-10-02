# 1672. Richest Customer Wealth
# You are given an m x n integer grid accounts where accounts[i][j] is t
# he amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

from typing import List

def maximumWealth(accounts: List[List[int]]) -> int:
    maximum = accounts[0]
    value = 0

    for i in range(len(accounts)):
        if sum(accounts[i]) > sum(maximum):
            maximum = accounts[i]
    
    for i in range(len(maximum)):
        value += maximum[i]

    return value

accounts = [[2,8,7],[9, 1, 5],[3, 1,7]]
print(maximumWealth(accounts))