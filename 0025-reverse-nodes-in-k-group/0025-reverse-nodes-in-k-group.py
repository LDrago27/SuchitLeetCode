# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
    
        def reverseKElement(head):
            '''
            reverse k element and returns head ,tail and next of the k element group
            '''
            temp = head
            noEle = 1
            prev = None

            while temp!= None and noEle <= k:
                prev = temp
                temp = temp.next
                noEle += 1
            print(noEle)
            if noEle != k+1:
                return (head,prev,None)

            else:
                # We need to reverse it
                prev = None
                temp = head
                noEle = 1

                while temp != None and noEle <= k:
                    nextNode = temp.next
                    temp.next = prev
                    prev = temp
                    
                    temp = nextNode
                    noEle +=1

                return (prev,head,temp)

    
        temp = head
        newHead = None
        prev = None
        
        if k==1:
            return head

        while temp!=None:
            
            pHead,pTail,pNext = reverseKElement(temp)
            #print(pHead,pTail,pNext)
            if newHead == None:
                newHead = pHead
                prev = pTail

            else:
                prev.next = pHead
                prev = pTail

            temp = pNext
        return newHead
        