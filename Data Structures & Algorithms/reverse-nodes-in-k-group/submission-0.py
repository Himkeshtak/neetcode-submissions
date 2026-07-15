# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # a while loop in range of K
        # simple reverse the linked list implemnet taion till the k 
        # then assigninng the pointer to the next k part of the list 
        
        curr = head

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while curr:
            
            count = 0
            check = curr
            while check and count < k :
                check = check.next
                count += 1
            
            if count==k:
                group_tail = curr
                prev = None
                i = 0

                while i<k:
                    next_node = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next_node
                    i += 1

                prev_group_end.next = prev
                group_tail.next = curr
                prev_group_end = group_tail
            else:
                break

        return dummy.next