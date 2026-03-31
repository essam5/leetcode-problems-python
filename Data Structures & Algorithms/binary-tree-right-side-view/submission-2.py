# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque([root])

        while queue:
            right_side = None
            len_queue = len(queue)
            for i in range(len_queue):
                node = queue.popleft()
                if node:
                    right_side = node
                    # adding left first
                    queue.append(node.left)
                    # adding second right to make the node have the right node
                    queue.append(node.right)
            # because we insert left first and then right , so the last node 
            # will be the right node 
            # that's why we check and append after the loop on the level        
            if right_side:
                result.append(right_side.val)    

        return result         
                




        