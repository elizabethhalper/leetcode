# 605. Can Place Flowers

# You have a long flowerbed in which some of the plots are planted,
# and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty
# and 1 means not empty, and an integer n, return true if n new flowers can be
# planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # [1,0,0,0,0,0,0,1]
        num_planted = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_plot = (i == 0) or (flowerbed[i-1] == 0)
                right_plot = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
                if left_plot and right_plot:
                    flowerbed[i] = 1
                    num_planted += 1
        return num_planted >= n