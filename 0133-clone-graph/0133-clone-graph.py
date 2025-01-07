"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # Need a map of Node.val to actual Nodes and then we can go around constructing the graph

        if node is None:
            return None

        valueNodeMap = {}

        stack = [node]
        
        # No need for a visited since there are no repeated edge and self loops
        visited = set()
        while stack:
            currNode = stack.pop()
            if currNode in visited:
                continue

            visited.add(currNode)
            
            if currNode.val not in valueNodeMap:
                valueNodeMap[currNode.val] = Node(currNode.val)
            
            for nextNode in currNode.neighbors:
                stack.append(nextNode)

        
        stack = [node]
        visited = set()

        while stack:
            currNode = stack.pop()

            if currNode in visited:
                continue

            visited.add(currNode)

            for nextNode in currNode.neighbors:
                stack.append(nextNode)
                valueNodeMap[currNode.val].neighbors.append(valueNodeMap[nextNode.val])
        
        return valueNodeMap[node.val]

