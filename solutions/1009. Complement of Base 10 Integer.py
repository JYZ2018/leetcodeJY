class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0: return 1
        x=1
        while x<=n:
            #print(x,end=",")
            x<<=1
            #print(x,end=',')
            #print(n,end=',')
            #print((x-1)^n)
        return (x-1)^n
        
