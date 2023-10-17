# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        
        stack = []
        temp = head
        while temp != None:
            stack.append(temp)
            temp = temp.getNext()
            
        while stack:
            node = stack.pop()
            node.printValue()
            
            
        