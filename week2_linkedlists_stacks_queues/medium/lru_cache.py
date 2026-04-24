class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):
# We are using Linked List and Dictionary in order to achieve it in O(1) time
# Dictionaty key -> node gives O(1) of lookup
# Linked List HEAD <-> nodes <-> TAIL gives O(1) insert/remove + track order
# Dict tells where is the node
# Linked List handles REORDER and REMVOE node
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}

        #Linked List
        #Dummy Nodes
        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    #Linked List functions to ADD or remove nodes
    def _remove(self,node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def _add(self, node):
        nxt = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = nxt
        nxt.prev = node

# we using this function so if we have 3, 2, 1 so 3 is mRU and we need to put 1 again so the order will be 1, 3, 2
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        
        #get the node
        node = self.cache[key]

        self._remove(node)
        self._add(node)
        #move it to the front because it's just used
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self._remove(self.cache[key])
        
        # Create new node
        node = Node(key, value)
        self.cache[key] = node

        #Move it to the front
        self._add(node)

        #Check the capacity
        if len(self.cache) > self.capacity:
            #Last node Least REcently used
            lru = self.tail.prev

            self._remove(lru)
            del self.cache[lru.key]


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)# LRU Cache

