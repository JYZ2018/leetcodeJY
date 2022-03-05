class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                if nums[j]==0:
                    nums[j],nums[i]=nums[i],nums[j]
                j+=1
       
   #method 2 (somehow slower than method 1)
        # j=0
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         if nums[j]==0:
        #             nums[i],nums[j]=nums[j],nums[i]
        #         j+=1
    
    
    
    
    
    
    #method 1
        '''
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
        '''
        
                
            
'''     i,j=0,0
        while j<len(nums):
