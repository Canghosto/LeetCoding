# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True
        if q is None and p is None:
            return res

        if (q is None and p is not None) or (q is not None and p is None) or p.val != q.val:
            res = False
        else:

            if res == True and p.left is not None and q.left is not None:
                res = self.isSameTree(p.left, q.left)
            
            if res == True and p.right is not None and q.right is not None:
                res = self.isSameTree(p.right, q.right)
            
            if res == True and (p.left is not None and q.left is None) or (p.left is None and q.left is not None):
                res = False
            
            if res == True and (p.right is not None and q.right is None) or (p.right is None and q.right is not None):
                res = False

        return res