# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def dfs(root,lis):
            if not root:
                return
            
            dfs(root.left,lis)
         
            lis.append(root.val)
           
            dfs(root.right,lis)
        lis1,lis2=[] ,[]   
        dfs(root1,lis1)
        dfs(root2,lis2)
       
        lis1.extend(lis2)
        lis1.sort()
        return lis1
        
            
        
