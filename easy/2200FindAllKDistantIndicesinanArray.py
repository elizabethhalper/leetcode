# 2200. Find All K-Distant Indices in an Array

# You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.

# Return a list of all k-distant indices sorted in increasing order.

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
#        key_indices = []
        ret = []
        # INITIAL ATTEMPT: WORKS BUT O(2N)
#         for i in range(len(nums)):
#             if nums[i] == key:
#                 key_indices.append(i)
        
#         print(key_indices)
            
#         for i in range(len(nums)):
#             for j in key_indices:
#                 if abs(i-j) <= k:
#                     ret.append(i)
#                     break
        
#         return ret
        left = 0
        for i in range(len(nums)):
            if nums[i] == key:
                for j in range(max(left, i - k), min(len(nums),i+k+1)):
                    ret.append(j)
                left = min(len(nums), i + k + 1)
                # if all right part is included?
                if left == len(nums):
                    break

        return ret