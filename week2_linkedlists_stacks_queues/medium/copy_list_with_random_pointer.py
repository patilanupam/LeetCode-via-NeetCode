# Copy List with Random Pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        #Step 1: Creating New node for list
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        
        #Step 2: Assign Random pointer
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr= curr.next.next    
        
        #Step 3: Seperate Lists
        curr = head
        copy_head = head.next

        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
        return copy_head


