class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            #print(num)
            cur=abs(num)
            if nums[cur]<0:
                return abs(num)
            nums[cur]=-1*nums[cur]
            #print(nums)
        
        
        
        
        
        
        
        # use sort method
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i]==nums[i-1]:
        #         return nums[i]
        
