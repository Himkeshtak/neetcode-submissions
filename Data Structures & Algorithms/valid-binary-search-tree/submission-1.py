# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Method-1 BFS lagao . left and rright ko queue mein  dalte wakte condition daal do
        # Method-2 DFS Lagao (preorder traversal)
        # Method-3 DFS lagao (inorder traversal)
        node = root
        def preorder(node, low=float('-inf'), high=float('inf')):
            if node is None:
                return True
            if node:
                # Node must respect the boundaries set by its parent & ancestors
                if not (low < node.val < high):
                    return False
                # When moving left, the parent's val becomes the upper limit (high)
                # When moving right, the parent's val becomes the lower limit (low)
                return preorder(node.left, low, node.val) and preorder(node.right, node.val, high)
                

        return preorder(node)