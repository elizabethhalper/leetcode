# 1480. Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ret = []
        sum = 0
        for i in range(len(nums)):
            ret.append(sum + nums[i])
            sum += nums[i]

        return ret