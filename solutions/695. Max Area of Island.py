class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dr=[1,0,-1,0,1]
        r,c=len(grid),len(grid[0])
        self.area=0
        
        def dfs(grid,x,y,r,c):
            #print(x,y,count)
            if (x<0 or x>=r or y<0 or y>=c or grid[x][y]==0):
                #print("grid[x][y] is: ",grid[x][y])
                return 0
            self.area+=1
            #print(count)
            grid[x][y]=0
            for i in range(4):
                #print("here: ", x,y)
                xx=x+dr[i]
                yy=y+dr[i+1]
                #print("here: ", xx,yy)
                dfs(grid,xx,yy,r,c)
                
            return self.area
        
        max_area=float('-inf')
        for i in range(r):
            for j in range(c):
                self.area=0
                area=dfs(grid,i,j,r,c)
                #print(area)
                max_area=max(max_area,area)
        return max_area
       
                
        
