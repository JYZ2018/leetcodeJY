class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d_1,d_2={},{}
        res=[]
        for i in nums1:
            d_1[i]=d_1.get(i,0)+1
        for i in nums2:
            d_2[i]=d_2.get(i,0)+1
        for i in d_1.keys():
            if d_1[i]<d_2.get(i,0):
                res.extend(d_1[i]*[i])
            elif d_2.get(i)!=None:
                res.extend(d_2[i]*[i])
        #print(d_1,d_2)
        return res
                
                
        
        
