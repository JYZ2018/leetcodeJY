class Solution:
    def climbStairs(self, n: int) -> int:
        
        # most comfortable way
        zero=0
        one=1
        for i in range(1,n+1):
            temp=one
            one=one+zero
            zero=temp
        return one
            
            
            
        
        
       
    
    
    
    
    
    # qi
#         pre=0
#         before=1
#         curr=1
#         for i in range(1,n+1):
#             curr=pre+before
#             pre=before
#             before=curr
#         return curr
            
      
        
        # recursion exceed time limit
#         def fib(n):
#             if n==1:
#                 return 1
#             if n==2:
#                 return 2
