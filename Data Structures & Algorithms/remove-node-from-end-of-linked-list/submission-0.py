# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reading of the n starts from the Zero
        # it in rotatinfg pattern 
        # node to be deleted 
        curr = head
        prev = None
        #bef = None
        count = 0

        while curr != None:
            curr = curr.next
            count += 1

        curr = head
        target = count - n
        # to delete a given node
        for i in range(target+1):
            if i == target:
                if prev == None:
                    head = curr.next
                else:
                    prev.next = curr.next
                break
            bef = prev
            prev = curr
            curr = curr.next
        return head