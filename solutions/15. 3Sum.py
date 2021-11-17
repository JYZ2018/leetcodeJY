class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        print(nums)
        for i in range(len(nums)-2):
            if nums[i]!=nums[i-1] or i==0:
                left=i+1
                r=len(nums)-1
                
                while left<r:
                    
                    if (nums[left]+nums[r])<(0-nums[i]):
                        left=left+1
                        
                    elif (nums[left]+nums[r])>(0-nums[i]):
                        r=r-1
                        
                    else:
                        if nums[left]!=nums[left-1] or left==i+1:
                            result.append([nums[i],nums[left],nums[r]])
                        
                        
                        
                        left=left+1
                        r=r-1
              
        return result
