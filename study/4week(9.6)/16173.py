# 16173 (점프왕 젤리)
# 9:56 ~ 10:44
# 함수에서도 break문으로 탈출 가능?
import sys
input = sys.stdin.readline
n = int(input())
arr = []
is_possible = False
for i in range(n):
    arr.append(list(map(int, input().split())))

def bfs(row, col):
    ans = False
    if arr[row][col] == -1:
        # 탈출
        ans = True
    else:
        jump = arr[row][col]
        if jump != 0: # jump가 0일떄....!!! 
            row_cor = False
            col_cor = False
            if row + jump <= n-1:
                row_cor = bfs(row+jump, col)
            if col + jump <= n-1:
                col_cor = bfs(row, col+jump)
            if row_cor == True or col_cor == True:
                ans = True
    return ans

if n == 2:
    if arr[0][0] == 1:
        if arr[0][1] == 1 or arr[1][0] == 1:
            print("HaruHaru")
            is_possible = True
    if is_possible == False:
        print("Hing")

elif n == 3:
    if bfs(0,0):
        print("HaruHaru")
    else:
        print("Hing")


# 우선 함수 안에서의 전역 변수가 안 먹는 것 같다.
# 함수 안에서 if문 안에 변수를 사용했더니 적용 안 되는 듯. 
# 가장 중요한 조건 읽기 2<=n<=3, 그리고 jump가 0일수도 있다는 점.
# 함수 탈출 방법: return!!!! 

### 괜찮은 두번쨰 코드.
import sys
input=sys.stdin.readline

def dfs(x,y) :
    #영역을 벗어났거나 이미 방문을 했다면 return
    if x>=N or y>=N or visit[x][y]==1:
        return
    
    #방문한 곳의 이동 칸 수가 -1이라면 방문처리를 해주고 return 한다. 2번 다시 안하도록.
    if graph[x][y] == -1 :
        visit[x][y] = 1
        return

    #방문했다고 표시해준다.
    visit[x][y]=1

    #하단,우측을 요소 수만큼 점프하여 방문한다.
    dfs(x+graph[x][y],y)
    dfs(x,y+graph[x][y])

#게임 구역의 크기 N을 입력받는다.
N=int(input())

#게임판의 구역을 입력받는다. 2차원 리스트
graph=[list(map(int,input().split())) for _ in range(N)]

#방문여부를 저장할 visit 2차원 리스트를 만든다.
visit=[[0]*N for _ in range(N)]

#출발은 0,0에서 하므로 dfs(0,0)을 호출한다.
dfs(0,0)

#결과 출력 (visit[n-1][n-1])
if visit[-1][-1] == 1 :
    print('HaruHaru')
else :
    print('Hing')