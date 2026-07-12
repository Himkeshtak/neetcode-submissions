class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        count1, count2 = 0, 0  
        val1, val2 = 0, 0
        
        while curr1 != None:
            # FIX: Only multiply the CURRENT digit by its place value
            val1 += curr1.val * (10 ** count1)
            count1 += 1
            curr1 = curr1.next

        # loop for the second list
        while curr2 != None:
            # FIX: Only multiply the CURRENT digit by its place value
            val2 += curr2.val * (10 ** count2)
            count2 += 1
            curr2 = curr2.next
        
        output_val = val1 + val2
        
        # Now create the linked list for the output
        dummy = ListNode(0)
        curr_out = dummy

        # Watch out for the typo here too: 'ListNode' must have a capital 'N'
        if output_val == 0:
            return ListNode(0)

        while output_val > 0:
            digit = output_val % 10
            curr_out.next = ListNode(digit)
            curr_out = curr_out.next
            output_val //= 10
        
        return dummy.next