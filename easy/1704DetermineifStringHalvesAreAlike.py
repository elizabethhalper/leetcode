# 1704. Determine if String Halves Are Alike
# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

# Return true if a and b are alike. Otherwise, return false.

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = int(len(s)/2)
        a = s[0:mid]
        b = s[mid:len(s)]
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        count_a = 0
        count_b = 0
        for char in a:
            if char in vowels:
                count_a += 1
        
        for char in b:
            if char in vowels:
                count_b += 1
        
        return count_a == count_b