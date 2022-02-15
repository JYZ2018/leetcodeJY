class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid]>nums[right]:
                left=mid+1
            if nums[mid]<nums[right]:
                right=mid
            if nums[mid]==nums[right]:
                right=right-1
        return nums[left]
                
        
​
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# use low can't pass [10,1,10,10,10] 
        
       
#        left,right=0,len(nums)-1
#         while left<right:
#             mid=left+(right-left)//2
#             if nums[mid-1]>nums[mid]:
