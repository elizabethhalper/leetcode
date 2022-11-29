# Given the root of a binary tree, collect a tree's nodes as if you were doing this:

# Collect all the leaf nodes.
# Remove all the leaf nodes.
# Repeat until the tree is empty.

# Input: root = [1,2,3,4,5]
# Output: [[4,5,3],[2],[1]]
# Explanation:
# [[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output = collections.defaultdict(list)
        
        def dfs(node, layer):
            if not node:
                return layer
            left = dfs(node.left, layer)
            right = dfs(node.right, layer)
            layer = max(left, right)
            output[layer].append(node.val)
            return layer + 1
        
        dfs(root, 0)
        return output.values()
#         pairs = []
#         ret = []
        
#         pairs = self.getHeights(root, pairs)
#         pairs = sorted(pairs, key=lambda x: x[0])
        
#         i = 0
#         height = 0
#         while i < len(pairs):
#             nums = []
#             while i < len(pairs) and pairs[i][0] == height:
#                 nums.append(pairs[i][1])
#                 i += 1
#             ret.append(nums)
#             height += 1
#         return ret
        
        
#     def getHeights(self, root, pairs):
#         if not root:
#             return -1
#         left_height = self.getHeights(root.left, pairs)
#         right_height = self.getHeights(root.right, pairs)
        
#         curr_height = max(left_height, right_height)
#         pairs.append((curr_height, root))
        
#         return pairs
        