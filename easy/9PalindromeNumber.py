# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_len = len(x_str)
        for i in range(math.floor(x_len/2)):
            if x_str[i] != x_str[x_len-i-1]:
                return False
        return True