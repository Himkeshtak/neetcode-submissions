# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if not root:
            return []
        res = []        
        queue.append(root)
        while queue:
            rightmost = None
            for i in range(len(queue)):
                node = queue.popleft()
                rightmost = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(rightmost.val)
            
        return res