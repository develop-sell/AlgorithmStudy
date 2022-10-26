# 현수막
# 14716
# 7:44 ~ 7:52
from collections import deque
n,m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]


ans = 0
dy = [-1,+1,+0,+0,-1,+1,-1,+1] # 상 하 좌 우 우상 우하 좌상 좌하
dx = [+0,+0,-1,+1,+1,+1,-1,-1]

def bfs(y,x):
    global ans
    
    qu = deque()
    qu.append((y,x))
    while qu:
        ny, nx = qu.popleft()
        for i in range(8):
            nny = ny + dy[i]
            nnx = nx + dx[i]
            if 0<=nny<n and 0<=nnx<m and visited[nny][nnx] == 0 and board[nny][nnx] == 1:
                qu.append((nny,nnx))
                visited[nny][nnx] = -1
    
    ans += 1
    

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and board[i][j] == 1:
            bfs(i,j)


print(ans)