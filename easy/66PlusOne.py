# 66. Plus One

#You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in
# left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # non-edge case
        addoneindex = len(digits) - 1
        digits[addoneindex]+=1
        while addoneindex > 0 and digits[addoneindex] == 10:
            digits[addoneindex] = 0
            addoneindex-=1
            digits[addoneindex]+=1
        
        if digits[0] == 10:
            digits[0]=0
            digits.insert(0,1)

        return digits
