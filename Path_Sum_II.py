# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.final = []
        def check_sum(root,sum_,list_):
            if root is None:
                return
            # print(root.val,sum_)
            temp = sum_-root.val
            
            if root.left is None and root.right is None and temp == 0:
                self.final.append(list_ + [root.val])
                return
            
            check_sum(root.left,temp,list_ + [root.val])
            check_sum(root.right,temp,list_ + [root.val])
            return
        check_sum(root,targetSum,[])
        return self.final