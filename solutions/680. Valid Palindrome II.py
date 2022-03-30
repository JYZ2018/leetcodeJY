class Solution:
   
    def validPalindrome(self, s: str) -> bool:
        def isvalid(s):
            l,r=0,len(s)-1
            while l<r:
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True
            
     
        l,r=0,len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return isvalid(s[l+1:r+1]) or isvalid(s[l:r])
        return True
                  
                
        
        
        
        
        
        
        '''
        l,r=0,len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1;r-=1
            else:
