# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.visit = 0

        def dfs(node):
            if not node:
                return 0    

            left = dfs(node.left)
            right = dfs(node.right) 
            if abs(left - right) > 1:
                self.visit +=1
            return 1 + max(left, right)    

        dfs(root)

        return True if self.visit == 0 else False      
  

        
        # go to the last leaf and get the height 
        # in recursion if you made the process after recursion 
        # the process begin impact for the deepth thing not for the first element
        # create a balance variable to get the True or false 
        # return with adding + 1 to the height (this is the process)

        def dfs(node):
            if not node:
                return [True, 0]

            left, right = dfs(node.left), dfs(node.right)

            balance = ((abs(left[1] - right[1]) <= 1) and
                        (left[0] and right[0]))

            return [balance, 1 + max(left[1], right[1])] # we need the heightest to check if the next compare greater than one after subtraction or not                 
    
        return dfs(root)[0]