class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        if len(needle)>len(haystack):
            return -1
        
        max_l,j=0,0
        
        for i in range(len(haystack)):
            if haystack[i]==needle[j]:
                temp=i
                r_h=i+len(needle)-1
                r_n=len(needle)-1
                #print("i,r_h,r_n is: ", end='')
                #print(i,r_h,r_n)
                if r_h>len(haystack)-1:
                    return -1
                else:
                    while i<=r_h:
                        if haystack[i]==needle[j] and haystack[r_h]==needle[r_n] :
                            i+=1
                            j+=1
                            r_h-=1
                            r_n-=1
                        else:
                            break
                        
                        
                        #print(i,r_h,j,r_n)
                if i==r_h+2 or i==r_h+1:
                    return temp
                else:
                    i=temp
                    j=0
        return -1
        
        
        
        
