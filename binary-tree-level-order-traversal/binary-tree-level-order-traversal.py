# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        res = []
        temp = []
        queue = [root,'EOL']
        if root == None:
            return res
        
        while queue:
            ele = queue.pop(0)
            
            if ele == 'EOL':
                res.append(temp)
                if queue:
                    queue.append('EOL')
                temp = []
                continue
            
            temp.append(ele.val)
            
            if ele.left!= None:
                queue.append(ele.left)
            if ele.right!= None:
                queue.append(ele.right)
        
        return res
                
            
            