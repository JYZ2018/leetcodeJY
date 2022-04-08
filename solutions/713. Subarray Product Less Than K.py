class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res=0
        l,product=0,1
        for r in range(len(nums)):
            product*=nums[r]
            #print(product,res,l,r)
            while product>=k and l<=r:
                # print(res,l,r)
                product=product/nums[l]
                l+=1
            res+=r-l+1
        return res
