class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result=[]
        if nums[0]>=0:
            for i in range(len(nums)):
                result.append(nums[i]**2)
            return result
        if nums[len(nums)-1]<=0:
            for i in range(len(nums)-1,-1,-1):
                result.append(nums[i]**2)
            return result
        div=-1
        for i in range(len(nums)):
            if nums[i]>=0:
                div=i
                break
        #print(div)
        
        j=div-1
        
        #print(j)
        while (j>=0 and div<len(nums)):
            if nums[div]<nums[j]*(-1):
                result.append(nums[div]**2)
                div=div+1
                
                #print(result)
            else:
                result.append(nums[j]**2)
                j=j-1
                #print(result)
            
          
        if j==-1:
            for i in range(div,len(nums)):
                result.append(nums[i]**2)
               
        if div==len(nums):
            for i in range(j,-1,-1):
                result.append(nums[i]**2)
              
        return result
                
                
        
        
