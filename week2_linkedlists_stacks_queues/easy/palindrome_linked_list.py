# Palindrome Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        
        # Logic same as LinkedList Cycle Floyd Hare TOrtoise method
        #Step 1  is to find middle element
        slow= head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        # Reverse Second Half
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #Step3 Compare both values
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True 

