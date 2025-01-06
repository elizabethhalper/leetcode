# 345. Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear
# in both lower and upper cases, more than once.

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        word_vowels = []
        for c in s:
            if c.lower() in vowels:
                print(c.lower())
                word_vowels.append(c)
        
        count = 0
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i].lower() in vowels:
                s_list[i] = word_vowels[len(word_vowels)-1-count]
                count += 1
        ret = "".join(s_list)

        return ret