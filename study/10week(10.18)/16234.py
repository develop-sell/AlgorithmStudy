# 인구 이동 16234
# 9:25- 10:03 (recur error)
# 10:09 (dfs->bfs로 변경해서 80% 시초)
# 10:10 pypy로 돌리니까 맞음

from collections import deque
import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**6)#재귀 깊이 늘려줌
ans = -1 # 인구 며칠

n, l, r = map(int, input().split()) #보드크기, 몇 이상, 몇 이하

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

'''
dfs로 진행해야하고. dfs로 arr에 계속 해당 위치 추가할 것. 
추후 나중에 for문 돌면서 arr에 len만큼 나눈 값을 해당 값들로 변경해준다. 

move에는 union1, union2 ...가 존재한다
union은 [(1,2), (2,3)] 이런식으로 존재. 
'''

exit = False
visited = []
union = []
move = []
def init():
    global visited
    global move
    visited = [[0 for _ in range(n)] for _ in range(n)] # 초기화 필요.
    move = []

dy = [-1,+1,+0,+0] # 상 하 좌 우
dx = [+0,+0,-1,+1]

# def dfs(y,x):
#     global union
#     union.append((y,x)) # 자기 자신 추가.
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
        
#         if 0<=ny<n and 0<=nx<n and visited[ny][nx] == 0:
#             if l<= abs(board[y][x] - board[ny][nx]) <=r:
#                 visited[ny][nx] = -1
#                 dfs(ny,nx)

def bfs(y,x):
    global union
    qu = deque()
    qu.append((y,x))
    while qu:
        cur = qu.popleft()
        ny = cur[0]
        nx = cur[1]
        union.append((ny,nx)) # 자기 자신 추가 
        for i in range(4):
            nny = ny + dy[i]
            nnx = nx + dx[i]
            
            if 0<=nny<n and 0<=nnx<n and visited[nny][nnx] == 0:
                if l<= abs(board[ny][nx] - board[nny][nnx]) <=r:
                    visited[nny][nnx] = -1
                    qu.append((nny, nnx))
                
def pmove():
    global move
    global ans
    if move:
        for uunion in move:
            people = 0
            # uunion = [(1,2),(2,3)]
            for point in uunion:
                people += board[point[0]][point[1]]
            cpeople = people // len(uunion)
            
            for point in uunion:
                board[point[0]][point[1]] = cpeople
                
    else:
        return True

    return False
    
while not exit:
    init()
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = -1
                bfs(i,j) # 이게 끝나면 union 초기화
                if len(union) != 1:
                    move.append(union) # 새로운 union 추가. (len가 1이면 자기자신만 있는 것)
                union = [] # dfs가 끝나면 union도 새로 변경
    
    exit = pmove()
    ans += 1

print(ans)