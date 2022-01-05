​
​
​
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        #solution 2 BFS
        m, n = len(grid), len(grid[0])
        DIR = [0, 1, 0, -1, 0]
    
        def bfs(r, c):
            if grid[r][c] == "0": return 0
            q = deque([(r, c)])
            #print("q is: ", end=",")
            #print(q)
            while q:
                r, c = q.popleft()
                #print(r,c)
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i+1]
                    if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] == "0": continue
                    grid[nr][nc] = "0"  # Mark as visited
                    q.append([nr, nc])
                    #print(q)
            return 1
    
        ans = 0
        for r in range(m):
            for c in range(n):
                ans += bfs(r, c)
        return ans
        
        
        
        #solution 1 DFS
        '''
