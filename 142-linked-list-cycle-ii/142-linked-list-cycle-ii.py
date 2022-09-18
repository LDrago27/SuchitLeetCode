# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
                
        if head== None or head.next==None:
            return None       
        
        sptr = head
        fptr = head
        while fptr!= None and fptr.next!=None:
            sptr = sptr.next
            fptr = fptr.next.next
            if sptr==fptr:
                break
            #print('Yp')    
        
        if fptr != sptr:
            return None
        
        sptr = head
        print(fptr.val,sptr.val)
        
        while sptr!=fptr:
            sptr=sptr.next
            fptr =fptr.next
            
        return sptr
        
            
            
            