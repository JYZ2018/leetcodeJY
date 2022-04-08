class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        resL=float('inf')
        sum,l=0,0
        for r in range(len(nums)):
            sum+=nums[r]
            while sum>=target:
                resL=min(resL,r-l+1)
                sum-=nums[l]
                l+=1
        if resL==float('inf'):
            return 0
        return resL
            
        
