# 2354. Number of Excellent Pairs
# You are given a 0-indexed positive integer array nums and a positive integer k.

# A pair of numbers (num1, num2) is called excellent if the following conditions are satisfied:

# Both the numbers num1 and num2 exist in the array nums.
# The sum of the number of set bits in num1 OR num2 and num1 AND num2 is greater than or equal to k, where OR is the bitwise OR operation and AND is the bitwise AND operation.
# Return the number of distinct excellent pairs.

# Two pairs (a, b) and (c, d) are considered distinct if either a != c or b != d. For example, (1, 2) and (2, 1) are distinct.

# Note that a pair (num1, num2) such that num1 == num2 can also be excellent if you have at least one occurrence of num1 in the array.

# TODO: THIS WORKS BUT RUNS OUT OF TIME

class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        fin = 0
        j = len(nums) - 1
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            for j in range(len(sorted_nums)-1,-1,-1):
                if j < len(sorted_nums) - 1 and sorted_nums[j] == sorted_nums[j+1]:
                    continue
                set_and = self.countSetBits(sorted_nums[i]&sorted_nums[j])
                set_or = self.countSetBits(sorted_nums[i]|sorted_nums[j])
                if set_and + set_or >= k:
                    fin += 1
                    
        return fin
    
    def countSetBits(self, n: int):
        count = 0
        while (n):
            count += n & 1
            n >>= 1
        return count