# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_min(self, root):

        while root.left:
            root = root.left
        return root    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        check for the greater than or less than 
        but if we found 
        check for the exsit with right and left 
        find the min 
        replace the values and delete the 
        """
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None

            if not root.left:
                return root.right

            if not root.right:
                return root.left

            # find min    
            successor = self.find_min(root.right) 

            root.val = successor.val

            root.right = self.deleteNode(root.right, successor.val) 

        return root                       
        