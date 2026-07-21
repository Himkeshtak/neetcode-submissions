# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')

        def inorder(node):
            nonlocal prev
            if not node:
                return True
            
            # 1. visit left
            if not inorder(node.left):
                return False
            
            #2. check current node vs previous node
            if node.val <= prev:
                return False
            
            prev = node.val # update previous value

            # 3. visit right
            return inorder(node.right)

        return inorder(root)
        