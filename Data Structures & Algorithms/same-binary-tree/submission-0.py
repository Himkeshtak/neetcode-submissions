# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # do the BFS based level order traversal and then if andy value or 
        # the structure mismatches then return the False
        #q = deque()
        #if root:
        #    q.append(root)
        #
        #level = 0
        #while q:
        #    for i in range(len(q)):
        #        node = q.popleft()  # as this is a queue it removes the element form the begininning
        #        if node.left:
        #            q.append(node.left)
        #        if node.right:
        #            q.append(node.right)
        #    level += 1

        p_queue, q_queue = deque(),deque()
        if p:
            p_queue.append(p)
        if q:
            q_queue.append(q)

        level_p , level_q = 0 , 0

        while p_queue or q_queue:

            if len(p_queue) != len(q_queue):
                return False

            for i in range(len(p_queue)):
                
                node_p , node_q = p_queue.popleft(), q_queue.popleft()
                
                if node_p is None and node_q is None:
                    continue

                if node_p is None or node_q is None or node_p.val != node_q.val:
                    return False

                if node_p.left or node_q.left:
                    p_queue.append(node_p.left) 
                    q_queue.append(node_q.left) 
                
                if node_p.right or node_q.right:
                    p_queue.append(node_p.right) 
                    q_queue.append(node_q.right) 

            level_p += 1
            level_q += 1

        return True 