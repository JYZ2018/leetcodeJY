class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=set()
        res=set()
        for i in nums1:
            if i not in s:
                s.add(i)
        for j in nums2:
            if j in s:
                res.add(j)
        return res
            
        
