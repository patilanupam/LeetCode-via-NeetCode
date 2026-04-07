# Remove Linked List Elements

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head

        current = dummy

        # thinking:
        # always look at next node, not current
        # so we can "skip" it if needed

        while current.next:
            if current.next.val == val:
                # skip the node
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next
