# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res=[]
       
        curr=root
        q = deque([])
        
        while  curr or len(q)>0:
           
            while curr:
                q.append(curr)
                curr=curr.left
            curr=q.pop()
            res.append(curr.val)
            curr=curr.right
            
        return res
        
        
        '''
        self.result=[]
        
        def helper(root):
            if not root:
                return 
            helper(root.left)
            self.result.append(root.val)
            helper(root.right)
         
        helper(root)
        return self.result
        '''
