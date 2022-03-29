class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        # same method as meeting room 2
        
        
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
                res.append([start[s-1],end[e]])
        return res
        
