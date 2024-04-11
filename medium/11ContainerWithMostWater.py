# 11. Container With Most Water

# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints
# of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.

# Return the maximum amount of water a container can store.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)-1):
            for j in range(i, len(height)):
                new_poss = self.computeArea(height[i], height[j], i, j)
                if new_poss > max_area:
                    max_area = new_poss
        
        return max_area
        
    def computeArea(self, iVal: int, jVal: int, i: int, j: int) -> int:
        h = min(iVal, jVal)
        l = j - i
        return h*l