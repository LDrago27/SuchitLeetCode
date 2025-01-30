# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2Lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeUtil(start,end):

            if start >end:
                return None
            if start == end:
                return lists[start]
            elif end == start+1:
                return self.merge2Lists(lists[start],lists[end])

            mid = (start+end) // 2
            return self.merge2Lists(mergeUtil(start,mid),mergeUtil(mid+1,end))

        n = len(lists)
        return mergeUtil(0,n-1)



        