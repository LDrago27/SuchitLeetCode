"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        
        def height(root):
            
            if root == None:
                return 0
            
            res = 1
            for child in root.children:
                res = max(res, 1 + height(child))
                
            return res
        
        def findDiameter(root):
            
            if root == None:
                return 0
            
            # include the current node in the result
            
            htList = []
            diaList = []
            
            for child in root.children:
                htList.append(height(child))
                diaList.append(findDiameter(child))
            
            htList.sort(reverse = True)
            n = len(htList)
            res = 0
            for i in range(min(2,n)):
                res = res + htList[i]
            
            if diaList:
                return max(max(diaList),res)
            return res
        
        return findDiameter(root)
        
                
            