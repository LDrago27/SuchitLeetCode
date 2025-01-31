# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class AugTreeNode:
    def __init__(self, val=0, left=None, right=None, ctr = 1):
        self.val = val
        self.left = left
        self.right = right
        self.ctr = ctr

    def __repr__(self):
        if self is None:
            return "None-"
        return f"<Test val:{self.val} left:{self.left} right:{self.right} ctr:{self.ctr}>"

class Solution:

    def constructAugmentedTree(self, root):
        if root is None:
            return None
        elif root.left is None and root.right is None:
            return AugTreeNode(root.val)
        leftSide = self.constructAugmentedTree(root.left)
        rightSide = self.constructAugmentedTree(root.right)
        currCtr = 1 + (leftSide.ctr if leftSide else 0) + (rightSide.ctr if rightSide else 0)
        return AugTreeNode(root.val,leftSide,rightSide,currCtr)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # Dumb Idea: In order traversal and then determine it 
        # Augmented Tree -> each node now contains a new element i.e no of elements just below it  
        augTreeHead = self.constructAugmentedTree(root)


        def findK(root,k):
            
            greaterEle = root.right.ctr if root.right else 0
            smallEq = root.ctr - greaterEle
            if  smallEq == k:
                return root.val
            elif smallEq > k:
                return findK(root.left,k)
            else:
                return findK(root.right,k-smallEq)

        #print(augTreeHead)
        return findK(augTreeHead,k)