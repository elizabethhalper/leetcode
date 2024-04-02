# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_hash = {}
        for i in range(len(nums)):
            if nums[i] in num_hash:
                return True
            else:
                num_hash[nums[i]] = i

        return False