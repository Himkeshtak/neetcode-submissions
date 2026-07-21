# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Use the inroder traversal
        #prev = float('inf')
        vis = 0 
        K = k 
        def inorder(node):
            nonlocal K
            nonlocal vis
            if not node:
                return None

            left_res = inorder(node.left)
            if left_res is not None:
                return left_res

            vis += 1
            if vis == K:
                return node.val
           
            return inorder(node.right)

        return inorder(root)