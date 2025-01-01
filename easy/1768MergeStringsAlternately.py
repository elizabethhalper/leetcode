# 1768. Merge Strings Alternately

# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order,
# starting with word1. If a string is longer than the other,
# append the additional letters onto the end of the merged string.

# Return the merged string.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        w1_i, w2_i, m_i = 0, 0, 0
        merged = ""
        while w1_i < len(word1) and w2_i < len(word2):
            if m_i % 2 == 0:
                merged += word1[w1_i]
                w1_i += 1
            else:
                merged += word2[w2_i]
                w2_i += 1
            m_i += 1
        if w1_i >= len(word1):
            merged += word2[w2_i:]
        else: # w1 >= len(word1):
            merged += word1[w1_i:]
        return merged