# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # we will de simple pre order traversal ad on each step will check if it
        # is a good node or not.
        self.good_nodes_count = 0
        def preorder(node, max_val):
            if node is None:
                return
            if node.val >= max_val:
                self.good_nodes_count += 1
            
            #update the max value for the child paths
            max_val = max(max_val, node.val)
            
            preorder(node.left, max_val)
            preorder(node.right, max_val)

        preorder(root, root.val)
        return self.good_nodes_count