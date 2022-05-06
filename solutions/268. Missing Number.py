class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # return (set(range(len(nums)+1))-set(nums)).pop()
        
        sum,n=0,len(nums)
        for i in nums:
            sum+=i
        #print(sum)
        return int((n*(n+1))/2-sum)
            
            
        
