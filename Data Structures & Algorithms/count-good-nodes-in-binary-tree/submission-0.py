# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
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
        