# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue=deque()
        queue.append(root)
        
        res=[]
        left=True
        
        while len(queue)!=0:
            lst=[]
            queue_len=len(queue)
            for i in range(queue_len):
                node=queue.popleft()
                lst.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if left:
                res.append(lst)
            else:
                res.append(lst[::-1])
            left=not left
        
        return res
            
        
        
        
