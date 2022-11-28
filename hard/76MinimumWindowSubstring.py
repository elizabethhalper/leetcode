# 76. Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # store all unique chars in dict
        dict_t = Counter(t)
        # required number of chars
        required = len(dict_t)
        # number of t chars in s
        num_char_t_in_s = 0
        # dict of t chars in window (so we know if we can decrement)
        window_counts = {}
        # values that will create our return val
        ret_helper = float("inf"), None, None
        
        r = 0
        l = 0
        # move right pointer to right until "desireable"
        while r < len(s):
            new_char = s[r]
            # add one to dict/count of char in window
            window_counts[new_char] = window_counts.get(new_char, 0) + 1
            
            # if frequency of new_char is desired count in t then inc num_char_t_in_s by 1
            # ie make windoww "desireable"
            if new_char in dict_t and window_counts[new_char] == dict_t[new_char]:
                num_char_t_in_s += 1
            
            print(s[l:r])
            while l <= r and num_char_t_in_s == required:
                new_char = s[l]
                
                # save smallest window
                if r-l + 1 < ret_helper[0]:
                    ret_helper = (r-l+1,l,r)
                
                # start moving window
                window_counts[new_char] -= 1
                if new_char in dict_t and window_counts[new_char] < dict_t[new_char]:
                    num_char_t_in_s -= 1
                
                # move left pointer
                l += 1
                print(s[l:r])

            # move right pointer
            r+=1
            print(s[l:r])

        # return min window
        return "" if ret_helper[0] == float("inf") else s[ret_helper[1]:ret_helper[2]+1]
