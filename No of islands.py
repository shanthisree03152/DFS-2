#DFS 
#TC: O(m*n) - n is no of rows, m is no of cols
#SC: o(m*n), worst case if all are 1's

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #null check
        if len(grid) <= 0 or grid is None:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]] 
        
        count = 0
        
        def dfs(grid, curx, cury):
            
            #base
            if curx < 0 or curx >= n or cury < 0 or cury >= m or grid[curx][cury] == '0':
                    return
                
            #logic 
            grid[curx][cury] = '0'    
            for direc in dirs:
                nr = direc[0] + curx
                nc = direc[1] + cury
                
                helper(grid, nr, nc)
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count
    
#BFS
#TC: O (m*n) - n is no of rows, m is no of cols
#SC: o(min(m, n)), even in worst case if all are 1's, 
# max elements in queue is diagnol of grid which is min(m, n)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #null check
        if len(grid) <= 0 or grid is None:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]] 
        
        count = 0
        q = deque()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    q.append([i,j])
                    count += 1
                    
                #logic
                while q:
                    curx, cury = q.pop() 
                    for direc in dirs:
                        nr = direc[0] + curx
                        nc = direc[1] + cury
                        
                        if nr >= 0 and nr < n and nc >= 0 and nc < m and grid[nr][nc] == '1':
                            grid[nr][nc] = '0'
                            q.append([nr,nc])
                
        return count