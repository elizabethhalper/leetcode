# 53. Maximum Subarray == medium
# Given an integer array nums, find the subarray which has the largest sum and return its sum.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = 0
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)-1):
            for j in range(i, len(nums)):
                new_sum = self.calcSum(i, j, nums)
                if new_sum > max_num:
                    max_num = new_sum
        
        return max_num

    def calcSum(self, i: int, j: int, nums: List[int]):
        fin = 0
        for n in range(i,j+1):
            fin+=nums[n]
        
        return fin