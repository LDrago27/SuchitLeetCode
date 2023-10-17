"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        
        def deepClone(root):
            
            if root == None:
                return None
            
            else:
                newRoot = Node(root.val)
                
                for child in root.children:
                    newRoot.children.append(deepClone(child))
                
                return newRoot
            
        return deepClone(root)