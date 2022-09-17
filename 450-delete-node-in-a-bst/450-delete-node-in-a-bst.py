# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        

        
        def findMinNode(root):
            if root == None:
                return float('inf')
            
            return min(root.val,findMinNode(root.left),findMinNode(root.right))
            
        
        def deleteNodeUtil(root,key):
            
            if root == None:
                return root
            
            if root.val == key:
                if root.left == None and root.right == None:
                    return None
                
                if root.left == None:
                    temp = root.right
                    root = None
                    return temp
                
                if root.right == None:
                    temp = root.left
                    root = None
                    return temp
                
                minVal = findMinNode(root.right)
                root.val = minVal
                root.right = deleteNodeUtil(root.right,minVal)
            
            elif root.val > key:
                root.left = deleteNodeUtil(root.left,key)
            else:
                root.right = deleteNodeUtil(root.right,key)
            return root
            
        return deleteNodeUtil(root,key)
                
        