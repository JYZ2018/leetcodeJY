class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r=len(board)
        c=len(board[0])
        visited = set()
        
        def dfs(board,i,j,visited):
            if i<0 or i>=r or j<0 or j>=c or board[i][j]=='X' or board[i][j]=='*' or (i,j) in visited:
                return
            
            visited.add((i,j))
            board[i][j]='*'
            dfs(board,i-1,j,visited)
            dfs(board,i,j-1,visited)
            dfs(board,i+1,j,visited)
            dfs(board,i,j+1,visited)
       
        for i in range(r):
            for j in range(c):
                #print(0,i,j)
                if (i==0 or j==0 or i==r-1 or j==c-1) and board[i][j]=='O':
                    #print(1,i,j)
                    dfs(board,i,j,visited)
                    
        for i in range(r):
            for j in range(c):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='*':
                    board[i][j]='O'
        return board
                
                    
        
        
        
        
        
        
        
        
        
        
        
#         r=len(board)-1
#         c=len(board[0])-1
              
