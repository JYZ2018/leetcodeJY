class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        dr=[1,0,-1,0,1]
        r,c=len(board),len(board[0])
        count=0
        for i in range(r):
            
            for j in range(c):
                #print("i,j is:",i,j)
                if board[i][j]=='R':
                    #print("here")
                    break
            if board[i][j]=='R':
                    #print("here")
                    break
            
        #print(i,j)
        for n in range(4):
            #print(n)
            x=i+dr[n]
            y=j+dr[n+1]
            #print(x,y)
            while (0<=x<r and 0<=y<c):
                if board[x][y]=='.':
                    x=x+dr[n]
                    y=y+dr[n+1]
                elif board[x][y]=='B':
                    break
                elif board[x][y]=='p':
                    count+=1
                    break
        return count
        
