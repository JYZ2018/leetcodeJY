class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if trust==[]:
            if n==1:
                return n
            else:
                return -1
        record_j={}
        record_c={el:0 for el in range(1,n+1)}
        for t in trust:
            
            record_c[t[0]]=1
                
            if t[1] not in record_j:
                record_j[t[1]]=1
            else:
                record_j[t[1]]+=1
          
        print(record_j)
        print(record_c)
        for r in range(1,n+1):
            if record_c[r]==0 and (r in record_j) and record_j[r]==n-1:
                return r
        return -1
            
        
