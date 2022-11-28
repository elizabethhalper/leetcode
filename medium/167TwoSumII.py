# 167. Two Sum II - Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low_itr = 0
        high_itr = len(numbers) - 1
        while (low_itr < high_itr):
            sum_val = numbers[low_itr] + numbers[high_itr]
            if sum_val == target:
                return[low_itr+1, high_itr+1]
            if sum_val < target:
                low_itr += 1
            if sum_val > target:
                high_itr -= 1
        return[-1,-1]