class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        
        
        
        #  three pointers
        # i,j,k=m-1,n-1,m+n-1
        # while i>=0 and j>=0:
        #     if nums1[i]>=nums2[j]:
        #         nums1[k]=nums1[i]
        #         i-=1
        #     else:
        #         nums1[k]=nums2[j]
        #         j-=1
        #     k-=1
        #     #print(i,j,k)
        #     #print(nums1)
        # if j>=0:
        #     nums1[:j+1]=nums2[:j+1]
        
        
        
        # wrong, can't use for loop, then i -=1 for every step
        # k=n+m-1
        # for i in range(m-1,-1,-1):
        #     if nums1[i]>=nums2[n-1]:
        #         nums1[k]=nums1[i]
        #     else:
        #         nums1[k]=nums2[n-1]
        #         n-=1
        #     k-=1
        #     print(m,n,k)
        #     print(nums1)
        
        
        
#         if m==0:
#             nums1[m]=nums2[m]
      
#         index=n+m-1
#         while m>0 and n>0:
#             if nums1[m-1]<=nums2[n-1]:
#                 nums1[index]=nums2[n-1]
#                 n-=1
#             else:
#                 nums1[index]=nums1[m-1]
#                 m-=1
#             index-=1
            
