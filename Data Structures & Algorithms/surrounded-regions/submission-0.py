class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        change = set()

        def bfs(r, c):
            q = deque()
            visited = set()
            q.append((r, c))
            while q:
                y, x = q.popleft()
                visited.add((y, x))
                for dr, dc in directions:
                    dy, dx = dr + y, dc + x
                    if not (0 <= dy < rows) or not (0 <= dx < cols):
                        return None
                    elif (dy, dx) not in visited and board[dy][dx] != 'X':
                        q.append((dy, dx))
                        visited.add((dy,dx))
            return visited
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in change:
                    mp = bfs(r, c)
                    if mp:
                        for i in mp:
                            change.add(i)

        if change:
            for y, x in change:
                board[y][x] = 'X'
        
                