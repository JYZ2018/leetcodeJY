class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        for i in range(len(nums)):
            if nums[i]!=nums[j]:
                j+=1
                nums[j]=nums[i]
                #print(j)
        return j+1
        
        
        
#         j=0
#         for i in range(len(nums)):
#             if nums[i]!=nums[j]:
#                 nums[j+1]=nums[i]
#                 j+=1
#         return j+1
       
            
                
        
        
        
        
        
        
        
        
        
        
