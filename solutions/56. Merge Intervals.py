class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[]
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i-1][1]<intervals[i][0]:
                res.append(intervals[i])
            else:
                intervals[i][0]=intervals[i-1][0]
                intervals[i][1]=max(intervals[i][1],intervals[i-1][1])
                res.pop()
                res.append(intervals[i])
            #print(intervals)
        return res
                
        
