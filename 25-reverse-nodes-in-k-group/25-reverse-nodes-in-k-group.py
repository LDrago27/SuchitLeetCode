# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(head):
            prev = None
            temp = head
            
            while temp != None:
                nextNode = temp.next
                temp.next = prev
                prev = temp
                temp = nextNode
                
            # now prev is current head and end is head
            return [prev,head]
        
        

        prev = None
        temp = head
        newHead = None
        
        while temp!= None:
            ctr =1
            start = temp
            while temp!=None and ctr<k:
                temp = temp.next
                ctr+=1
            if ctr==k and temp!=None:
                nextNode = temp.next

                temp.next = None

                khead,kend = reverse(start)

                if prev == None:
                    newHead = khead
                else:
                    prev.next = khead

                prev = kend

                prev.next = nextNode
                temp = nextNode
    
        return newHead
            
            
                