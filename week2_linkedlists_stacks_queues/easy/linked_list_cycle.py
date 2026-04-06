# Linked List Cycle
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #FLOYD CYCLE: TORTISE AND HARE APPROACH
        slow = head
        fast = head

        while fast and fast.next:
            # As fast traverse one step ahead
            slow = slow.next
            fast = fast.next.next

            # If slow and fast meets the cycle exists
            if slow == fast:
                return True
            
        return False
# Time Complexity: O(n) 
# Space Complexity: O(1)
