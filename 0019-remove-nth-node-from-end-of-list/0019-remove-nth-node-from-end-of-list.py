# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Step 1: Finding the n th node from the start 
        # Idea 1: Compute the netLength of list and find netLength- k node from the start -> Not too elegant not too demure
        # Idea 2: two pointer baby , sptr fptr -> starts from n position and moves 
        # Since it is a removal of a node we definetley need a prevnode
        if head is None:
            return None

        prevNode = None
        fptr = sptr = head
        ctr = 1

        while ctr <=n and fptr:
            fptr = fptr.next
            ctr+=1
        #print(fptr)
        while fptr and sptr:
            prevNode = sptr
            sptr = sptr.next
            fptr = fptr.next
        
        if prevNode is None:
            # We are removing the damn head
            return head.next

        prevNode.next = sptr.next # removed sptr

        return head

            