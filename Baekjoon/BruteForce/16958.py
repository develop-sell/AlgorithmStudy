# 텔레포트(16958) 11.29(화)
# 1:02-1:54
'''
일반적으로 가는 행위와 텔레포트 거치는 행위 2가지의 최소값 구하는 것

알게 된 점:
1. bfs로 돌리면 1000*1000번을 확인하기에 시간초과가 난다.
 - 따라서 O(n) 시간 되도록 텔레포트만 따로 모아둔 리스트를 도는 것이 빠르다

2. break 의문.
 - 현재의 cnt가 min 값을 넘을 때 해당 가지를 버린다.
 - 빨라지긴 하지만, 과연 필요한 부분일까? 
 - 최악의 테케가 100개 있을 때의 시간을 기준으로 하지 않을까?
 - 그렇다면 시간을 줄이는게 의미가 있을까? 
 - 만약 저렇게했는데 시간초과가 나면,
 - 다른 방법이 있지 않을까라고 생각하는 것이 좋아보인다.

'''

from collections import deque

n, t = map(int, input().split())

city = [0] * 1001
teleport = []
for i in range(n):
    s, x, y = map(int, input().split())
    city[i+1] = (y,x)
    if s == 1:
        teleport.append((y,x))

def findMinTel(y,x):
    # O(n)
    min_val = 10000
    for t in teleport:
        min_val = min(min_val, abs(t[0]-y) + abs(t[1]-x))
    return min_val

for j in range(int(input())):
    s, e = map(int, input().split())
    ans = abs(city[s][0] - city[e][0]) + abs(city[s][1] - city[e][1])
    ss = findMinTel(city[s][0], city[s][1]) # 시작점에서 가장 가까운 텔레포트 거리
    ee = findMinTel(city[e][0], city[e][1]) # 끝점에서 가장 가까운 텔레포트 거리 
    ans2 = ss+ee+t
    print(min(ans, ans2))

'''
y,x에서 가장 가까운 텔포 지점을 리턴하는 값. 

bfs -> 100만개인데.
일반 1000개면? 그게 낫지 않을까?
'''
# def findMinTel(y,x,max):
#     visited = [[0 for _ in range(1001)] for _ in range(1001)]
    
#     qu = deque()
#     qu.append((y,x,0))
#     ans = max # 최대값.
#     while qu:
#         ny,nx,cnt = qu.popleft()
#         if ans > cnt:
#             if board[ny][nx] == 1:
#                 ans = min(ans, cnt)
#             else:
#                 for i in range(4):
#                     nny = ny + dy[i]
#                     nnx = nx + dx[i]
#                     if 0<=nny<=1000 and 0<=nnx<=1000 and visited[nny][nnx] == 0:
#                         visited[nny][nnx] = -1
#                         qu.append((nny,nnx,cnt+1))
                        
#     return ans


    
'''
반례
6 3
0 1 2
0 5 1
0 3 3
0 1 5
0 3 5
0 7 5
5
1 2
1 5
1 6
3 4
4 2
'''

'''
해당 지점의 텔포만 탈 수 있다고 생각한 코드
'''
# n, t = map(int, input().split())
# city = [0] * 1000

# for i in range(n):
#     s, x, y = map(int, input().split())
#     city[i+1] = (s,x,y)

# a = []
# for j in range(int(input())):
#     s, e = map(int, input().split())
#     ans = abs(city[s][1] - city[e][1]) + abs(city[s][2] - city[e][2])
#     if city[s][0] == 1 and city[e][0] == 1:
#         ans = min(ans, t)
#     a.append(ans)

# print(a)