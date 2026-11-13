"""
Problem: Container With Most Water
Link: https://www.hellointerview.com/learn/code/two-pointers/container-with-most-water
Date: 2026-11-12 | Solved alone? Yes 
Pattern: two-pointers
Key insight: moving the left pointer when the right wall is greater than 
             the left wall because moving the taller wall only 
             shrinks the width and height stays capped by the shorter wall
             so always move the shorter one
Time: O(n)
Space:O(1)
Revisit: 
Miss: (bug: width = right instead of right - left)
"""

def getMaxContainer(heights):

    maxCapacity = 0
    left, right = 0, len(heights)-1
    while left < right:
        height = min(heights[left], heights[right]) #get the smaller height
        width = right - left
        capacity = width * height
        maxCapacity = max(maxCapacity, capacity)
        if heights[left] < heights[right]: #if left wall is smaller than right wall move one step to the right else move the one step to the ledt from the end
            left+=1
        else:
            right-=1

    return maxCapacity


heights = [1,8,6,2,5,4,8,3,7]
print(getMaxContainer(heights))
print(getMaxContainer([1,1]))                # 1
print(getMaxContainer([1,2,1])) 