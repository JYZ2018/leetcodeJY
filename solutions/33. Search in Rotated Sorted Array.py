class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            
            # if the mid in the left sorted array
            if nums[l]<=nums[mid]:
                if nums[mid]<target or nums[l]>target:
                    l=mid+1
                elif nums[l]<=target<nums[mid]:
                    r=mid-1
            else:
                if nums[mid]>target or nums[r]<target:
                    r=mid-1
                elif nums[mid]<target<=nums[r]:
                    l=mid+1
        return -1
                
        
        
        
        
        
        
        
        
        
        # need more understanding
        '''
        left,right=0,len(nums)-1
        while left<right:
            mid=left+(right-left)//2
