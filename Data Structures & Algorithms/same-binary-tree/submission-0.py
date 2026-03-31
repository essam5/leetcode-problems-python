# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # bfs ---> get every level of both and compare 

        queue_1 = deque([p])
        queue_2 = deque([q])

        while queue_1 and queue_2:
            node_1 = queue_1.popleft()
            node_2 = queue_2.popleft()

            if not node_1 and not node_2:
                continue
            if not node_1 or not node_2 or node_1.val != node_2.val:
                return False

            queue_1.append(node_1.left)
            queue_1.append(node_1.right)
            queue_2.append(node_2.left)        
            queue_2.append(node_2.right)

        return True            


               
        