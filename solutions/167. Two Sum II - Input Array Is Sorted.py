class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(numbers)):
            if numbers[i] not in d:
                d[target-numbers[i]]=i
            else:
                return [d[numbers[i]]+1,i+1]
        
