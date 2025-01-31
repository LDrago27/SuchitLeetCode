# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preOrderIndex = [0]

        def constructTree(start,end):

            if start > end:
                return None
            elif start == end:
                preOrderIndex[0]+=1
                return TreeNode(inorder[start])
            else:

                rootVal = preorder[preOrderIndex[0]]
                preOrderIndex[0]+=1
                inOrderIndex = end+1

                for i in range(start,end+1):
                    if inorder[i] == rootVal:
                        inOrderIndex = i 
                        break


                return TreeNode(rootVal,constructTree(start,inOrderIndex-1),constructTree(inOrderIndex+1,end))
        
        n = len(inorder)
        return constructTree(0,n-1)
