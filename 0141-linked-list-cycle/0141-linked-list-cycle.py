# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Idea is we index all the nodes into a set and check if the node has occured before in the set or Not
        # TIme : O(n), Space : O(n)

        # Clever Approach 
        # Have 2 pointers a fast pointer and a slow pointer , if the fast and slowptr ever meet there is a cycle 

        fptr = sptr = head

        while fptr and sptr:

            sptr = sptr.next
            if fptr.next: 
                fptr = fptr.next.next 
            else:
                return False

            if fptr == sptr:
                return True
        return False
        