# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Divide and Conquer : No of groups O(nlogn)
        
        def merge2List(head1,head2):
            if head1 == head2:
                return head1
            elif head1 == None:
                return head2
            elif head2 == None:
                return head1
            
            temp1,temp2 = head1, head2
            newHead, curr = None, None
            
            while temp1!= None and temp2!=None:
                
                newNode = None
                
                if temp1.val > temp2.val:
                    newNode = temp2
                    temp2 = temp2.next
                else:
                    newNode = temp1
                    temp1 = temp1.next
                    
                if curr == newHead == None:
                    curr = newNode
                    newHead = curr
                else:
                    curr.next = newNode
                    curr = curr.next
            
            while temp1!= None:
                curr.next = temp1
                curr = curr.next
                temp1 = temp1.next
                
            while temp2!= None:
                curr.next = temp2
                curr = curr.next
                temp2 = temp2.next
                
            curr.next = None
            
            return newHead
        
        
        def mergeList(start,end):
            if end < start:
                return None
            if start == end:
                return lists[start]
            
            if end-start == 1:
                return merge2List(lists[start],lists[end])
            mid = (start+end) // 2
            return merge2List(mergeList(start,mid),mergeList(mid+1,end))
        
        n = len(lists)
        return mergeList(0,n-1)
            
        
        