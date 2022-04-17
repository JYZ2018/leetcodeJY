class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d_r={}
        
        for a in ransomNote:
            d_r[a]=d_r.get(a,0)+1
        for b in magazine:
            if b in d_r:
                d_r[b]-=1
        for a in d_r:
            if d_r[a]>0:
                return False
        return True
        
