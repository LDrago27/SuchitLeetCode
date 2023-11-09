# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # lets use divide and conquer
        
        def merge2List(head1,head2):
            
            # merge list1 and list2 and return list as  the sorted list
            
            temp1,temp2 = head1, head2
            
            newHead = None
            prev = None
            
            while temp1!= None and temp2!=None:
                
                if temp1.val <= temp2.val:
                    if newHead == None:
                        newHead = temp1
                    if prev == None:
                        prev = temp1
                    else:
                        prev.next = temp1
                        prev = temp1
                        
                    temp1 = temp1.next
                    

                else:
                    
                    if newHead == None:
                        newHead = temp2
                    if prev == None:
                        prev = temp2
                    else:
                        prev.next = temp2
                        prev = temp2
                        
                    temp2 = temp2.next
                    
            while temp1 != None:
                if newHead == None:
                    newHead = temp1
                if prev == None:
                    prev = temp1
                else:
                    prev.next = temp1
                    prev = temp1      
                temp1 = temp1.next
                
            while temp2!=None:
                if newHead == None:
                    newHead = temp2
                if prev == None:
                    prev = temp2
                else:
                    prev.next = temp2
                    prev = temp2      
                temp2 = temp2.next
            
            return newHead
        
        
        n = len(lists)
        
        def mergeUtil(start,end):
            if start > end or start> n or end > n:
                return None
            if start == end:
                return lists[start]
            
            mid = (start+end) // 2
            
            return merge2List(mergeUtil(start,mid),mergeUtil(mid+1,end))
        
        return mergeUtil(0,n-1)
            
                