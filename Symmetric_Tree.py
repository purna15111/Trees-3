# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.final = []
        self.check = True
        def check(temp1,temp2):
            if (temp1 is None and temp2 is not None) or (temp2 is None and temp1 is not None):
                self.check = False
                return
            if temp1 is not None and temp2 is not None and temp1.val != temp2.val:
                self.check = False
                return
            if temp1 is None and temp2 is None:
                return
            check(temp1.left,temp2.right)
            check(temp1.right,temp2.left)
        
        check(root.left,root.right)
        return self.check