class ListNode:
    def __init__(self,key,val,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key
    
class LRUCache:

    def __init__(self, capacity: int):
        # We will use a combination of hashMap and bidrectional linked list for this
        # This will allow us to do all the operations in O(1)
        self.map = {} # key -> list reference
        self.head = None
        self.end = None
        self.cap = capacity
        

    def get(self, key: int) -> int:
        
        # fetch the value and put it in first
        if key not in self.map:
            return -1
        
        else:
            node = self.map[key]
            
            # make the node as the new head
            # update the end
            
            # Case1 the node isalredy the head
            if node == self.head:
                return self.map[key].val
            elif node == self.end:
                self.end = node.prev
                node.prev.next = None
                node.prev = None
            else:
                # Somewhere in the middle
                prevNode = node.prev
                nextNode = node.next
                node.prev = None
                node.next = None
                prevNode.next = nextNode
                nextNode.prev = prevNode
            
            node.next = self.head
            self.head.prev = node
            self.head = node
            
            return self.map[key].val

    def put(self, key: int, value: int) -> None:
        
        # Can be didivide into two parts one is update / add and next is puting on first this can be done using the get
        
        # Update 
        if key in self.map:
            self.map[key].val = value
        
        # addition
        else:

            # Do we have capacity
            if len(list(self.map.keys())) < self.cap:
                self.map[key] = ListNode(key,value)
            else:
                self.map.pop(self.end.key)
                if self.end.prev!=None:
                    self.end = self.end.prev
                    self.end.next = None
                else:
                    self.end = None
                self.map[key] = ListNode(key,value)

                
            # Now we add the new stuff at the end
            if self.end == None:
                self.head = self.end = self.map[key]
            else:
                self.end.next = self.map[key]
                self.map[key].prev = self.end
                self.end = self.map[key]
                
        self.get(key)
                
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)