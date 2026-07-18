# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        if root:
            q.append(root)
        
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()  # as this is a queue it removes the element form the begininning
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level


        # here we use the BFS in which we are basically doing the level by level
        # traversal in the tree