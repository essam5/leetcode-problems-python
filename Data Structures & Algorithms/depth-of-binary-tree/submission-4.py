# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        depth = 0

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth +=1
        return depth            

























        # bfs , new queue , add root , 
        # loop for each level , add children for next level 
        if not root:
            return 0
        queue = deque([root])
        level = 0

        while queue:
            # stay on one level
            for i in range(len(queue)):
                node = queue.popleft()
                # add children to loop for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level +=1

        return level            















        
        #dfs 
        if not root:
            return 0    

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))   

        # bfs                 
        # init, if found level added to queue to count 

        # level = 0

        # queue = deque([root])

        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)

        #     level += 1

        # return level         

        # dfs stack 
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res       
            



                  
        