class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        if m==0:
            nums1[m]=nums2[m]
      
        index=n+m-1
        while m>0 and n>0:
            if nums1[m-1]<=nums2[n-1]:
                nums1[index]=nums2[n-1]
                n-=1
            else:
                nums1[index]=nums1[m-1]
                m-=1
            index-=1
            
        if n>=1:
            nums1[:n]=nums2[:n]
            
                
            
            
        