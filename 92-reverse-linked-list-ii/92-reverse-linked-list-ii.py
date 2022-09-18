# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        def reverse(head):
            if head == None:
                return head
            
            temp = head
            prev = None
            
            while temp!= None:
                nextNode = temp.next
                temp.next = prev
                prev = temp
                temp = nextNode
            
            #head and end of a list
            return [prev,head]
        
        prevEle = None
        
        temp = head
        ctr = 1
        
        while temp!=None and ctr<left:
            prevEle = temp
            temp = temp.next
            ctr+=1
        
        nextEle = None
        
        while temp!=None and ctr<right:
            temp = temp.next
            ctr+=1
        
        nextEle = temp.next
        temp.next = None
        
        if prevEle == None:
            newHead,newEnd = reverse(head)
        else:
            newHead,newEnd = reverse(prevEle.next)
        
        if prevEle == None:
            newEnd.next = nextEle
            return newHead
        else:
            prevEle.next = newHead
            newEnd.next = nextEle
            return head
        
        
                

                