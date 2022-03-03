class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left,right=1,len(arr)-2
        while left<=right:
            mid=left+(right-left)//2
            if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid-1]<arr[mid]:
                left=mid+1
            else:
                right=mid-1
        return left
    
    
    
        # method 1
        #return arr.index(max(arr))
        
