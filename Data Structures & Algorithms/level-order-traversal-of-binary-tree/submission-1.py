# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        #level = 0
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            current_level = []
            for i in range(len(queue)):
                node = queue.popleft()

                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
           
            res.append(current_level)
                
        return res