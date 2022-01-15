# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans=None
        
        def dfs(root,p,q):
            if not root:
                return False
            
            left=dfs(root.left,p,q)
            right=dfs(root.right,p,q)
            mid= root==p or root==q
            
            if left+right>=2:
                self.ans=root
​
            return mid or left or right
        
        dfs(root,p,q)
        return self.ans
        
        
        
