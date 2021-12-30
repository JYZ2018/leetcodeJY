class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        index,max_l,i=0,0,0
        count={}
        while i<len(s):
            
            #print(i)
            if s[i] not in count:
                count[s[i]]=1
                
            else:
                count[s[i]]+=1
                
            
            #print(count)
            if count[s[i]]>1:
                
                max_l=max(max_l,i-index)
                #print(i,index,max_l)
                index+=1
                i=index
                
                count.clear()
                #print(i,index,max_l)
            else:  
                i+=1
            max_l=max(max_l,i-index)
                
        return max_l
    
        
