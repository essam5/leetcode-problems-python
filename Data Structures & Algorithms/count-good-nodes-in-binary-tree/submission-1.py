# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # using  DFS 
        # move to the the path if we found value greater than 
        # max previous value that consider as a good node 

        def dfs(node, max_val):
            if not node:
                return 0

            res = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)

            return res

        return dfs(root, root.val)          















        """
        add a queue with two field , the second field reflect 
        to the max_val remember (-100 <= Node.val <= 100)
        add count and check if found node == or greater than the max add the count
        """
        count = 0
        queue = deque()
        queue.append((root, -float('inf')))
        while queue:
            node, max_val = queue.popleft()
            if max_val <= node.val:
                count +=1

            if node.left:
                queue.append((node.left, max(max_val, node.val)))
            if node.right:
                queue.append((node.right, max(max_val, node.val)))
        return count                
        