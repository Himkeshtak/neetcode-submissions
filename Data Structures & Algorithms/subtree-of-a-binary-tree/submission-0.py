# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we wil do the BFS traversal on the main tree and then when any node is 
        # equal to the root node of the subroot tree then we start the comaparisions too
        # that if each node of the Tree must be equal to all the nodes of the subtree

        r_queue, s_queue = deque(), deque()

        if root:
            r_queue.append(root)
        if subRoot:
            s_queue.append(subRoot)
            

        while r_queue:
            for i in range(len(r_queue)):
                
                node_r = r_queue.popleft()

                if node_r.val == subRoot.val:

                    p_queue = deque([node_r])
                    q_queue = deque([subRoot])
                    is_match = True

                    while p_queue or q_queue:
                        if len(p_queue) != len(q_queue):
                            is_match = False
                            break
                        
                        for j in range(len(p_queue)):
                            p_node = p_queue.popleft()
                            q_node = q_queue.popleft()

                            if not p_node and not q_node:
                                continue
                            if not p_node or not q_node or p_node.val != q_node.val:
                                is_match = False
                                break

                            if p_node.left or q_node.left:
                                p_queue.append(p_node.left)
                                q_queue.append(q_node.left)
                             
                            if p_node.right or q_node.right:
                                p_queue.append(p_node.right)
                                q_queue.append(q_node.right)
                             
                        if not is_match:
                            break
                    if is_match:
                        return True
                    
                    


                
            if node_r.left:
                r_queue.append(node_r.left)
                
            if node_r.right:
                r_queue.append(node_r.right)
                
        return False
                

