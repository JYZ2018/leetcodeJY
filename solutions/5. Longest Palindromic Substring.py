class Solution:
    def longestPalindrome(self, s: str) -> str:
        sr=''
        for i in range(0,len(s)):
            sr=sr+'|'+s[i]
        sr=sr+'|'
        
        center=0
        radius=0
        pa=[]
        
        while center<len(sr):
            while center-(radius+1)>=0 and center+(radius+1)<len(sr) and sr[center-(radius+1)]==sr[center+(radius+1)]:
                radius+=1
            pa.append(radius)
            
            
            oldcenter=center
            oldradius=radius
            radius=0
            center=oldcenter+1
            while center<=oldcenter+oldradius:
                mirrorcenter=oldcenter-(center-oldcenter)
                maxradius=oldcenter+oldradius-center
                if pa[mirrorcenter]<maxradius:
                    pa.append(pa[mirrorcenter])
                    center=center+1
                elif pa[mirrorcenter]>maxradius:
                    pa.append(maxradius)
                    center=center+1
                else:
                    radius=maxradius
                    break
                
        pali_len=max(pa)
        pali_center=pa.index(max(pa))
        #print(pa)
        #print(pali_len)
        #print(pali_center)
        #print(int (pali_center-int((pali_len-1)/2)))
        return sr[(pali_center-pali_len):(pali_center+pali_len+1)].replace('|','')
                
                
            
        
            
                
        
