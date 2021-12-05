class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1 or len(s)==0:
            return s
        
        #if len(s)==2 and s[1]==s[0]:
            #return s
        
        sn=''
        for i in range(0,len(s)-1):
            if i==0:
                s0=s[0]
                
            if s[i]==s[i]:
                a=i-1
                b=i+1
                while a>=0 and b<=len(s)-1 and s[a]==s[b]:
                    sn=s[a:b+1]
                    a=a-1
                    b=b+1
                   
                if len(sn)>len(s0):
                    s0=sn
                
            if s[i]==s[i+1]:
                a=i
                b=i+1
               
                while a>=0 and b<=len(s)-1 and s[a]==s[b]:
                    
                    sn=s[a:b+1]
                    a=a-1
                    b=b+1
                    
                if len(sn)>len(s0):
                    s0=sn
       
            
        return s0
            
            
                
        
