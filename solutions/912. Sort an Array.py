class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def partition(nums,low,high):
            #print(low,high)
            i=low
           
            for j in range(low,high+1):
                if nums[j]<nums[high]:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
                    #print(nums)
            nums[i] ,nums[high] =nums[high] ,nums[i] 
            #print(1)
            return i
        
        low,high=0,len(nums)-1
        def quicksort(nums,low,high):
            mid=(low+high)//2
            nums[mid],nums[high]=nums[high],nums[mid]
            if low<high:
                i=partition(nums,low,high)
                quicksort(nums,low,i-1)
                quicksort(nums,i+1,high)
            
        quicksort(nums,low,high)
        return nums
    
                    
                    
                    
                    
                    
                
        
        
