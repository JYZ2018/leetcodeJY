class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def sort(nums,start,end):
           
                mid=start+(end-start)//2
                nums[mid],nums[end]=nums[end],nums[mid]
                for i in range(start,end):
                    
                    #print("start,i,end are: ",start,i,end)
                    if nums[i]<nums[end]:
                        #print('2',nums[start],nums[i],nums[end])
                        nums[i],nums[start]=nums[start],nums[i]
                        start+=1
                #print("start is: ",start)
                   
                nums[start],nums[end]=nums[end],nums[start]
                #print(nums)
                return start
        def quicksort(nums,start,end):
            if start>=end:
                return
            #print("start,end is: ",start,end)
            partition=sort(nums,start,end)
            
            
            #print("2 start,end is: ",start,end)
            quicksort(nums,start,partition-1)
            #print("3 start,end is: ",start,end)
            quicksort(nums,partition+1,end)
               
        
        quicksort(nums,0,len(nums)-1)
        #print(nums)
        return nums[-k]
        
        
            
        
