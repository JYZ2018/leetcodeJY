class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        # alan
        sub={}
        l=0
        max_sub=0
        for i in range(len(s)):
            if s[i] in sub:
                l=max(sub[s[i]]+1,l)
            sub[s[i]]=i
            
            max_sub=max(i-l+1,max_sub)
            #print(l,i,sub,max_sub,i-l+1)
        return max_sub
                
            
        
        
        
        
        
        
        
        # neetcode
        # sub=set()
        # l,res=0,0
        # for r in range(len(s)):
