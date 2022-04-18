class Solution:
    def climbStairs(self, n: int) -> int:
        pre=0
        before=1
        curr=0
        i=1
        while i<=n:
            curr=pre+before
            pre=before
            before=curr
            i+=1
        return curr
            
            
            
            
            
        
        
    
        
        # recursion exceed time limit
#         def fib(n):
#             if n==1:
#                 return 1
#             if n==2:
#                 return 2
#             return fib(n-1)+fib(n-2)
#         return fib(n)
​
​
        
        
