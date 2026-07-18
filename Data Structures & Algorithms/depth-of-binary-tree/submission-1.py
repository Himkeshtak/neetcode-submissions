# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        stack = [[root, 1]]
        res = 0

        while stack:  # this means that stack till the stack is not empty
            node, depth = stack.pop()
             
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

        # here the DFS was just atechniques used , not exact implementation of
        # DFS is here , therefore , and only the logic of traversing is used here

