# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        
        def findMid(head):
            
            if head == None:
                return head
            
            sptr = head
            fptr = head
            prevSptr = None
            
            while fptr!=None and fptr.next!=None:
                prevSptr = sptr
                sptr = sptr.next
                fptr = fptr.next.next
                
            return [sptr,prevSptr]
        
        def createBst(head):
            if head == None:
                return None
            mid,prevMid = findMid(head)
            
            
            if prevMid == None:
                return TreeNode(mid.val,createBst(None),createBst(mid.next))
            prevMid.next = None
            return TreeNode(mid.val,createBst(head),createBst(mid.next))
        return createBst(head)
            
        