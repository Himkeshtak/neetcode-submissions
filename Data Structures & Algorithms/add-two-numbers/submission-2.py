# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #traverse both the list wiht the multiplacation of each next with 10 and then adding 
        #giving the exact number 
        # add them 
        #output the answer in the unfolding manneer
        curr1 , curr2 = l1, l2
        count1 , count2 = 0 , 0  # number of nodes visited
        val1 , val2 = 0 , 0

        while curr1 != None:
            #additon of nodes value in the final value of this
            val1 += curr1.val * (10 ** count1)
            #val1 = val1 * (10 ** count1)  this is a logical flaw what i did
            count1 += 1

            curr1 = curr1.next

        #loop for the second list
        while curr2 != None:
            
            
            val2 += curr2.val * (10 ** count2)
           # val2 = val2 * (10 ** count2)
            count2 += 1

            curr2 = curr2.next
        
        output_val = val1 + val2
        #now to create the linked list for the output , we will create a dummy output list
        dummy = ListNode(0)
        curr_out = dummy

        if output_val == 0:
            return ListNode(0)

        while output_val > 0:
           digit = output_val % 10
           curr_out.next = ListNode(digit)
           curr_out = curr_out.next
           output_val //= 10
        
        return dummy.next





          
             