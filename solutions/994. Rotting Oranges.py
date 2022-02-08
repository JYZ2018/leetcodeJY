class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue=deque()
        r,c=len(grid),len(grid[0])
        good_orange=0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    good_orange+=1
                    
        if good_orange==0:
            return 0
        dr=[-1,0,1,0,-1] 
        min=0
        while  len(queue)!=0:
            lst=[]
            queue_len=len(queue)
            for i in range(queue_len):
                r_,c_=queue.popleft()
                for i in range(4):
                    x=r_+dr[i]
                    y=c_+dr[i+1]
                    if (0<=x<r  and 0<=y<c and grid[x][y]==1):
                        queue.append((x,y))
                        grid[x][y]=2
                        good_orange-=1
            min+=1          
        min-=1
        if good_orange>=1:
            return -1
        else:
            return min
        
        
