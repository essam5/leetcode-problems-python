# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        by using dfs 
        make dfs with depth , before resursion append to
         the result with depth index 

        """
        result = []
        if not root:
            return result

        def dfs(node, depth):
            if not node:
                return None
            if len(result) == depth:
                result.append([])    
            result[depth].append(node.val)
            if node.left:
                dfs(node.left, depth +1)
            if node.right:
                dfs(node.right, depth + 1)            
        dfs(root, 0)
        return result 
        """
        use bfs 
        first make a queue 
        adding the root
        make a result list 
        loop on the tree , and make level list and len_q 
        loop inside the level to append to the level values 
        if level append to the result  
        """
        queue = deque([root])
        result = []
        while queue:
            len_queue = len(queue)
            level = []

            for i in range(len_queue):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                result.append(level)

        return result                

        