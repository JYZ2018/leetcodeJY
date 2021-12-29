class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j=0,0
        while i<len(nums):
            if nums[i]==0:
                if nums[j]!=0:
                    nums[i],nums[j]=nums[j],nums[i]
                j+=1
            i+=1
            
        i,k=0,0
        while i<len(nums):
            if nums[i]!=2:
                if nums[k]==2:
                    nums[i],nums[k]=nums[k],nums[i]
                k+=1
                
            i+=1
                
        
        
           
    
    
    
    
    
    
    
        '''
        sum0,sum1,sum2=0,0,0
        for i in range(len(nums)):
            if nums[i]==0:
                sum0+=1
            elif nums[i]==1:
                sum1+=1
            else:
                sum2+=1
        #print(sum0,sum1,sum2)
        for i in range(len(nums)):
            if i<sum0:
                nums[i]=0
            elif i<sum1+sum0:
                nums[i]=1
            else:
                nums[i]=2
               
          '''  
            
