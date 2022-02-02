class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        
        
        p_dict={}
        res=[]
        for i in p:
            if i not in p_dict:
                p_dict[i]=1
            else:
                p_dict[i]+=1
        #print(p_dict)
        temp_dict={}
        for i in range(len(s)-len(p)+1):
            if i==0:
                for j in range(i,i+len(p)):
                    if s[j] not in temp_dict:
                        temp_dict[s[j]]=1
                    else:
                        temp_dict[s[j]]+=1
            if i>0:
                temp_dict[s[i-1]]-=1
                if temp_dict[s[i-1]]==0:
                    del temp_dict[s[i-1]]
                temp_dict[s[i+len(p)-1]]=temp_dict.get(s[i+len(p)-1],0)+1
            
            #print(i,temp_dict)
            if p_dict== temp_dict:
                res.append(i)
        return res
    
    
    
        
        #brute force
#         p_dict={}
#         res=[]
#         for i in p:
#             if i not in p_dict:
#                 p_dict[i]=1
#             else:
#                 p_dict[i]+=1
