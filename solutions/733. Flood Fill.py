class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        r,c=len(image),len(image[0])
        temp=image[sr][sc]
        dr=[1,0,-1,0,1]
        visited=set()
        
        def dfs(image,sr,sc,temp,newColor,visited):
            image[sr][sc]=newColor
            visited.add((sr,sc))
            dr=[1,0,-1,0,1]
            visited
            for i in range(4):
                #print(i)
                x=sr+dr[i]
                y=sc+dr[i+1]
                #print(x,y)
                if (x<0 or x>=r or y<0 or y>=c or image[x][y]!=temp or ((x,y) in visited) ):
                    continue
                dfs(image,x,y,temp,newColor,visited)
                
            
            
        
       
        dfs(image,sr,sc,temp,newColor,visited)
        return image
                    
            
        
