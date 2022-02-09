class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left,right=0,len(nums)-1
       
        res=[]
        
        while left<=right:
            #print(left,right)
            #print(res)
            mid=left+(right-left)//2
            #print(mid)
            
                
            if target>nums[mid]:
                left=mid+1
            elif target<nums[mid]:
                right=mid-1
                
            else:
                   
                if nums[left]==nums[right]:
                    res.append(left)
                    res.append(right)
                    return res
                    
                elif nums[left]<nums[mid]:
                    left+=1
                    
                elif nums[right]>nums[mid]:
                    right-=1
            #print("2:",left,right)
        return [-1,-1]
            
        
        
            
            
        
