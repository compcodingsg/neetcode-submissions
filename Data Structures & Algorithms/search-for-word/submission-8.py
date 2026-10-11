class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        n = len(board)
        m = len(board[0])

        def dfs(wi: int, visited: List[List[bool]], si: int, sj: int):
            
            if wi == len(word):
                return True
            
            res = False
            for dirn in dirs:
                ti = si+dirn[0]
                tj = sj+dirn[1]
                if 0 <= ti < n and 0 <= tj < m:
                    if not visited[ti][tj] and board[ti][tj] == word[wi]:
                        visited[ti][tj] = True
                        res = res or dfs(wi+1, visited, ti, tj)
                        visited[ti][tj] = False
            
            return res

        visited = [[False]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if dfs(1, visited, i, j):
                        return True
                    visited[i][j] = False
                
        
        return False

            
        