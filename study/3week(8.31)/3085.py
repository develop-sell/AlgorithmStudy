# 8:30~10:07
import sys
input = sys.stdin.readline
n = int(input())
candy = []
answer = 0
for i in range(n):
    candy.append(list(input().rstrip()))

def getMaxCandyLen(new_candy, direction, row, col):
    max_count = 0
    # n대신 len(new_candy)
    if direction == 0:
        # 오른쪽 변경
        # 가로 
        for j in range(n-1):
            count = 1
            for k in range(j+1,n):
                if new_candy[row][j] == new_candy[row][k]:
                    count += 1
                else:
                    max_count = max(max_count, count)
                    break
            max_count = max(max_count, count)
        # 세로 
        for new_col in range(col, col+2):
            for i in range(n-1):
                count = 1
                for k in range(i+1,n):
                    if new_candy[i][new_col] == new_candy[k][new_col]:
                        count += 1
                    else:
                        max_count = max(max_count, count)
                        break
                max_count = max(max_count, count)
    else:
        # 아래 변경
        # 가로 
        for new_row in range(row, row+2):
            for j in range(n-1):
                count = 1
                for k in range(j+1,n):
                    if new_candy[new_row][j] == new_candy[new_row][k]:
                        count += 1
                    else:
                        max_count = max(max_count, count)
                        break
                max_count = max(max_count, count)
        # 세로 
        for i in range(n-1):
            count = 1
            for k in range(i+1,n):
                if new_candy[i][col] == new_candy[k][col]:
                    count += 1
                else:
                    max_count = max(max_count, count)
                    break
            max_count = max(max_count, count)
    return max_count     
    
for i in range(n):
    for j in range(n):
        # 오른쪽과 변경
        if j != n-1:
            new_candy = [item[:] for item in candy]
            temp = new_candy[i][j] 
            new_candy[i][j] = new_candy[i][j+1]
            new_candy[i][j+1] = temp
            answer = max(answer, getMaxCandyLen(new_candy, 0, i, j))
        # 아래와 변경
        if i != n-1:
            new_candy = [item[:] for item in candy]
            temp = new_candy[i][j] 
            new_candy[i][j] = new_candy[i+1][j]
            new_candy[i+1][j] = temp
            answer = max(answer, getMaxCandyLen(new_candy, 1, i, j))
            
print(answer)

# 전역변수로 둬서 함수에서 쓸 수 없을까?
# 처음엔 아래, 위, 옆을 나눠서 진행함. 생각해보다 오른쪽과 아래만 하면 된다. 

# 스트링 입력 개행문자 제거하려면 rstrip 써야함.

# n-1 에서 n으로 바꿈. 

# deepcopy의 문제 -> [item[:] for item in candy] 시간 초과...