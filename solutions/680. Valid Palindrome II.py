def palindrome(s,change)  ->bool:
        l=0
        r=len(s)-1
       
        while  l<r: 
            if s[l]==s[r]:
                l=l+1
                r=r-1
            elif change==True:
                
                return (palindrome(s[l:r],False) or palindrome(s[(l+1):(r+1)],False))
            else:
                return False
        return True
        
​
​
​
class Solution:
    
    
    def validPalindrome(self, s: str) -> bool:
       
       return palindrome(s,True) 
                
        
​
        
        
                
            
            
        
