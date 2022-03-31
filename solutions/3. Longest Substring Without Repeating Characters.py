class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet=set()
        l,res=0,0
        for r in range(len(s)):
            
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res=max(res,r-l+1)
        return res
            
        
        
#         l,max_length=0,0
#         substring=set()
#         for r in range(len(s)):
#             if s[r] not in substring:
#                 substring.add(s[r])
                
#                 max_length=max(r-l+1,max_length)
#             else:
#                 while s[r] in substring:
#                     substring.remove(s[l])
#                     l+=1
#             substring.add(s[r])
            
#             print(l,r,max_length,substring)
