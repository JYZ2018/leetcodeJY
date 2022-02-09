class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left,right=0,len(nums)-1
        
        res=[]
        def binarysearch(left,right):
            while left<=right:
                mid=left+(right-left)//2
                #print(mid)
                if left==right and nums[mid]!=target:
                    return
                
                elif target>nums[mid]:
                    left=mid+1
                elif target<nums[mid]:
                    right=mid-1
                
                else:
                   
                    if nums[mid]==nums[left] and nums[mid]==nums[right]:
                        res.append(left)
                        res.append(right)
                        return
                    elif nums[left]<nums[mid]:
                        left+=1
                    
                    elif nums[right]>nums[mid]:
                        right-=1
            
        binarysearch(left,right)
        #print(res)
        if len(res)==0:
            return [-1,-1]
        else:
            return res
        
            
            
        
