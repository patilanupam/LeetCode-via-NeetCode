
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # curr = head
        # prev = None

        # while curr:
        #     nxt = curr.next      #tmp storing curr.next
        #     curr.next = prev     #curr.next to None
        #     prev = curr          # prev to current
        #     curr = nxt           # nxt assigned in tmp to curr 
        
        # return prev              #Loop continue till the list is reversed

        #Using Recursion

        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)

        head.next.next = head #Reverse the link
        head.next = None      # Broken the link

        return new_head
