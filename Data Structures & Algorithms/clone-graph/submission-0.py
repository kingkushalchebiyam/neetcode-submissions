"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        start = node
        stack = [start]

        visited = set()
        visited.add(start)


        if node is None: 
            return None

        while stack: 
            node = stack.pop()

            oldToNew[node] = Node(val=node.val)

            for neighbor in node.neighbors: 
                if neighbor not in visited: 
                    visited.add(neighbor)
                    stack.append(neighbor)
            
        
        for oldNode, newNode in oldToNew.items():
            for neighbor in oldNode.neighbors:
                newNeighbor = oldToNew[neighbor]
                newNode.neighbors.append(newNeighbor)


        return oldToNew[start] 





        

        