# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Assume we are always storing stuff in head1

        newHead = None
        currNode = None

        while list1 and list2:
            if list1.val >= list2.val:
                if not newHead:
                    currNode = newHead = list2
                else:
                    currNode.next = list2
                    currNode = currNode.next
                list2 = list2.next
            else:
                if not newHead:
                    currNode = newHead = list1
                else:
                    currNode.next = list1
                    currNode = currNode.next
                list1 = list1.next

        while list1:
            if not newHead:
                currNode = newHead = list1
            else:
                currNode.next = list1
                currNode = currNode.next
            list1 = list1.next
        while list2:
            if not newHead:
                currNode = newHead = list2
            else:
                currNode.next = list2
                currNode = currNode.next
            list2 = list2.next
        
        return newHead