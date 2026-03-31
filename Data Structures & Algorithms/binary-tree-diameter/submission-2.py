# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.max_diameter = 0
        
        def dfs(node):
            if not node:
                return 0

            height_left = dfs(node.left)
            height_right = dfs(node.right)

            self.max_diameter = max(self.max_diameter, height_left + height_right)

            return 1 + max(height_left, height_right)    
        dfs(root)

        return self.max_diameter

















        # dfs 
        # get hieght of left, right 
        # adding sum of this to the res if greater than res 
        # return the max of left or right + 1 the first node diameter
        self.max_diameter = 0
        def dfs(node):
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            self.max_diameter = max(self.max_diameter, left_height + right_height)

            return 1 + max(left_height, right_height)  

        dfs(root)

        return self.max_diameter      





















        
        self.max_diameter = 0 # make this self to access even if in method

        def dfs(current_node):
            if not current_node:
                return 0

            left = dfs(current_node.left)
            right = dfs(current_node.right)
            
            self.max_diameter = max(self.max_diameter, left+right)

            return 1 + max(left, right)

        dfs(root)

        return self.max_diameter    


        