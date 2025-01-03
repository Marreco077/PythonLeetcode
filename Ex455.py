# 455. Assign Cookies
# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie.
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child 
# will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the 
# cookie j to the child i, and the child i will be content. Your goal is to maximize the number 
# of your content children and output the maximum number.

from typing import List

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array [1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)


def findContentChildren(g: List[int], s: List[int]) -> int:
    g = quicksort(g)
    s = quicksort(s)

    child = 0
    cookie = 0

    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1
        cookie += 1

    return child

g = [10,9,8,7]
s = [5,6,7,8]
print(findContentChildren(g, s))