class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        
        left,right=0,len(nums)-1
        while left<right:
            mid=left+(right-left)//2
            #print(left,right,mid)
            if nums[mid]==target:
                return True
            if nums[mid]==nums[right]:
                right-=1
            elif nums[mid]>nums[right]:
                if target>nums[right]:
                    if nums[mid]>target:
                        right=mid-1
                    else:
                        left=mid+1
                else:
                    left=mid+1
            elif nums[mid]<nums[right]:
                if target>nums[right]:
                    right=mid-1
                else:
                    if nums[mid]>target:
                        right=mid-1
                    else:
                        left=mid+1
        #print("end: ",left,right,mid)
        if nums[left]==target:
            return True
        else:
            return False
          
            
            
            
            
            #compare with rightside, doesn't work 
        # left,right=0,len(nums)-1
        # while left<right:
        #     mid=left+(right-left)//2
