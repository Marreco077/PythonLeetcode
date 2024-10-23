from typing import List

def sortPeople(names: List[str], heights: List[int]) -> List[str]:
    n = len(heights)
    for i in range(n):
        for j in range(0, n-i-1):
            if heights[j] < heights[j+1]:
                heights[j], heights[j+1] = heights[j+1], heights[j]
                names[j], names[j+1] = names[j+1], names[j]
    
    return names

names = ["Alice", "Bob", "Charlie"]
heights = [155, 185, 150]
print(sortPeople(names, heights))
