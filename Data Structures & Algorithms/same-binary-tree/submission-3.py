# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack = [(p, q)]

        while stack: 
            a, b = stack.pop()

            if a is None and b is None: 
                continue
            

            if (a is None and b is not None) or (b is None and a is not None) or (a.val != b.val): 
                return False
            
            stack.append((a.right, b.right))
            stack.append((a.left, b.left))
        

        return True
            


            
        