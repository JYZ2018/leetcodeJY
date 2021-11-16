class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums_=[]
        for i in range(len(nums)):
            if nums[i] not in nums_:
                nums_.append(nums[i])
            
                temp={}
                rem=0-nums[i]
                for j in range(i+1, len(nums)):
                    if nums[j] not in temp:
                        temp[rem-nums[j]]=nums[j]
                    else:
                        l_s=[nums[i],rem-nums[j],nums[j]]
                        l_s.sort()
                        if l_s not in result:
                            result.append(l_s)
        return result
               
                
                
                
        
