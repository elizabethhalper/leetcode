# 1207. Unique Number of Occurrences
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_hash = {}
        count_hash = {}
        for i in range(len(arr)):
            if arr[i] in num_hash.keys():
                num_hash[arr[i]] += 1
            else:
                num_hash[arr[i]] = 1
        
        for key in num_hash.keys():
            if num_hash[key] in count_hash.keys():
                return False
            else:
                count_hash[num_hash[key]] = 1
            
        return True