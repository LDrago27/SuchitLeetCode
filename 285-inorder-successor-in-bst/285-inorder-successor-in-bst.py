# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        res = []
        def inOrderTraversal(root):
            if root== None:
                return 
            inOrderTraversal(root.left)
            res.append(root)
            inOrderTraversal(root.right)
            
        inOrderTraversal(root)
        n = len(res)
        for index in range(n):
            node = res[index]
            if node == p:
                break
                
        if index < n-1:
            return res[index+1]
        else:
            return None
            
            
            
                