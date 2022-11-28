# 153Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        fin = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSumforThreeSum(nums, i, fin)
        
        return fin
        
    def twoSumforThreeSum(self, numbers: List[int], i: int, fin: List[List[int]]) -> List[int]:
        low_itr = i + 1
        high_itr = len(numbers) - 1
        while low_itr < high_itr:
            sum_val = numbers[low_itr] + numbers[high_itr] + numbers[i]
            if sum_val == 0:
                fin.append([numbers[low_itr], numbers[high_itr], numbers[i]])
                low_itr += 1
                high_itr -= 1
                while low_itr < high_itr and numbers[low_itr] == numbers[low_itr - 1]:
                    low_itr += 1
            if sum_val < 0:
                low_itr += 1
            if sum_val > 0:
                high_itr -= 1
        return[]
#  what I wanted the answer to be but just doesn't work
#         hash = {}
#         fin = []

#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i != j:
#                     hash[nums[i]+nums[j]] = [i,j]
        
#         for k in range(len(nums)):
#             complement = 0 - nums[k]
#             if complement in hash.keys() and k != hash[0 - nums[k]][0] \
#                 and k != hash[0 - nums[k]][1]:
#                 fin.append([nums[hash[0 - nums[k]][0]], nums[hash[0 - nums[k]][1]], nums[k]])

#         return fin
        