class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
# method 3, use a temp to replace sum_2. more simple and elegant code same as method 2  
        sum_1,sum2=[1]*len(nums),[1]*len(nums)
    
        for i in range(1,len(nums)):
            sum_1[i]=sum_1[i-1]*nums[i-1]
        
        temp=1
        for i in range(len(nums)-2,-1,-1):
            temp=nums[i+1]*temp
            sum_1[i]=sum_1[i]*temp
            
        return sum_1
            
       
        
        
        
        
        
        
        
        
        
        
        
        
        
​
# 2 ways to generate list, here generate list with default value 1 is better, so we can set the last value of the list to 1. with empty list, you can't append the last value.
​
        # generate two list with default value
        sum_1,sum_2=[1]*len(nums),[1]*len(nums)
    
        # fill  sum_1 with multiplication results of all elements before nums[i] but not includes nums[i]
        # sum_1[0] is already default to 1
        for i in range(1,len(nums)):
