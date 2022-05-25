class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getSquare(n):
            squareSum=0
            for i in str(n):
                squareSum+=int(i)*int(i)
            return squareSum
        
        res=[n]
        if n==1:
            return True
       
        while True:
            n = getSquare(n)
            if n in res:
                return False
            res.append(n)
            
            if n==1:
                return True
            #print(n)
       
                
            
        
