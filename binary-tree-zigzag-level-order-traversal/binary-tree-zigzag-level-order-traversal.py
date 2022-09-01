# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res= []
        temp = []
        queue = [root,'EOL']
        ctr = 0
        
        if root == None:
            return res
        
        while queue:
            ele = queue.pop(0)
            
            if ele == 'EOL':
                if ctr%2 == 0:
                    res.append(temp)
                else:
                    res.append(temp[::-1])

                if queue:
                    queue.append('EOL')
                temp = []
                ctr+=1
                continue
            
            temp.append(ele.val)

            if ele.left!= None:
                queue.append(ele.left)
            if ele.right != None:
                queue.append(ele.right)
        
        return res
            
        