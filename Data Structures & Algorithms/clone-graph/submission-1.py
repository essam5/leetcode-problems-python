"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # usig bfs 
        """
        map visited 
        queue for node 
        loop and get the popleft which value 
        loop in the neighbors , added to visited, added to queue
        after that added to neighbors of this node 

        """
        if not node:
            return None
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val)

        while queue:
            n = queue.popleft() # processing node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])

        return visited[node]            
        """
        using dfs 
        check for empty 
        make visited map 
        dfs --> take a copy for node , and for neighbors 
        """

        if node is None:
            return None

        visited = {}

        def dfs(n):
            if n in visited:
                return visited[n]

            copy = Node(n.val)
            visited[n] = copy

            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)                
        