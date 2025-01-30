# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []


        res = []

        queue = [root]

        while queue:

            newQueue = []
            currLevel = []
            for node in queue:
                currLevel.append(node.val)

                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)
            res.append(currLevel)
            queue = newQueue[:]

        return res
