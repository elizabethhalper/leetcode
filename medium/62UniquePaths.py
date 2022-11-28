# 62. Unique Paths
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
#         recursive solution is correct but too slow
#         if m == 1 or n == 1:
#             return 1
        
#         ret = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
#         return ret
        ret = [[1] * n for j in range(m)]
        for col in range(1,m):
            for row in range(1,n):
                ret[col][row] = ret[col-1][row] + ret[col][row-1]
        
        return ret[m-1][n-1]