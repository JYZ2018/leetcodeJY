class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res,temp_max,temp_min=nums[0],nums[0],nums[0]
       
        
        for i in range(1,len(nums)):
            a,b=temp_max, temp_min
            temp_max=max(a*nums[i],b*nums[i],nums[i])
            temp_min=min(a*nums[i],b*nums[i],nums[i])
            #print(a,b,temp_max,temp_min)
            res=max(temp_max,res)
        return res
            
        
        
        
        
        
        
        
        
        
        
        #brute force, TLE
        '''
        product=float('-inf')
        for i in range(len(nums)):
            product_i=1
            for j in range(i, len(nums)):
                product_i=product_i*nums[j]
                product=max(product,product_i)
                #print(i,j,product)
