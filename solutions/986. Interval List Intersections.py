class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        
        res=[]
        i,j=0,0
        while i<len(firstList) and j<len(secondList):
            start=max(firstList[i][0],secondList[j][0])
            end=min(firstList[i][1],secondList[j][1])
            if start<=end:
                res.append([start,end])
            if firstList[i][1]>=secondList[j][1]:
                j+=1
            else:
                i+=1
        return res
        
        
        
        
        # same method as meeting room 2
        
        '''
        start=sorted([i[0] for i in firstList]+[i[0] for i in secondList])
        end=sorted([i[1] for i in firstList]+[i[1] for i in secondList])
        #print(start,end)
        res=[]
        count=0
        s,e=0,0
        while s<len(start):
            if start[s]<=end[e]:
                s+=1
                count+=1
            else:
                e+=1
                count-=1
            if count==2:
