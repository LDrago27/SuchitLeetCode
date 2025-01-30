# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Point: we need create a map of pos -> Node Or dumb thiong just put the damn thing into a array and then just rearrange them 
        # Time complexity - O(n) Space :O(1) not taking any additional space 

        nodeList = []
        temp = head

        while temp:
            nodeList.append(temp)
            temp = temp.next
        
        n = len(nodeList)
        
        newHead = prevNode = None
        lim = n//2 +1 if n%2 !=0 else n//2
        for i in range(lim):
            currNode = nodeList[i]

            if newHead is None:
                newHead = prevNode = currNode
            else:
                prevNode.next = currNode 

            prevNode = currNode

            if (n-i-1) != i:
                prevNode.next = nodeList[n-i-1]
                prevNode = prevNode.next
        
        prevNode.next = None

        return newHead

            





