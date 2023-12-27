class Node:
    def __init__(self,key,value,next = None,prev = None):
        self.val = value
        self.next = next
        self.prev = prev
        self.key = key
        

class LRUCache:
    # We will need a combination of maps and a Doubly Linked List
    # Doubly Linked List since they support O(1) additons and deletions
    # HashMap to find the exact Node that we need without the need for a scan 
    # These will help to keep an average time complexity of O(1) for all three operations

    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodeMap = {} # Maps keys to the actual Nodes
        self.head = self.end = None # Setting start and end of the Doubly Linked List to None

    def get(self, key: int) -> int:
        
        if key not in self.nodeMap:
            return -1 # No Key

        else:
            # fetch the key and push the node to the top 
            resNode = self.nodeMap[key] # searched Node
            value = resNode.val
            # Make it new Head

            if self.head == resNode:
                # case 1 : it is the head
                return value
            elif self.end == resNode: 
                # Case 2: it is an endNode
                self.end = resNode.prev 
                self.end.next = None
                resNode.prev = None

                resNode.next = self.head
                self.head.prev = resNode
                self.head = resNode
                return value
            else: # Case 3 : IT is a middle node
                prevNode = resNode.prev
                nextNode = resNode.next

                prevNode.next = nextNode
                nextNode.prev = prevNode

                resNode.next = self.head
                self.head.prev = resNode
                resNode.prev = None
                self.head = resNode
                return value


    def put(self, key: int, value: int) -> None:



        if key in self.nodeMap:

            self.nodeMap[key].val = value
            self.get(key)

        else:

            if self.cap <=0:
                # We need to pop out the last element and then 

                # Pop out the last endNode

                
                del self.nodeMap[self.end.key]

                if self.end == self.head:
                    self.end = self.head = None
                else:
                    endNode = self.end.prev
                    endNode.next = None
                    self.end.prev = None

                    self.end = endNode
                
                self.cap += 1

            self.cap -=1
            newNode = Node(key,value)
            self.nodeMap[key] = newNode

            if self.head == self.end == None:
                self.head = self.end = newNode
            else:
                self.end.next = newNode
                newNode.prev = self.end
                self.end = newNode
                self.get(key)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)