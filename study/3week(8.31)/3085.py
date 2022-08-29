# 8:30~
from copy import copy, deepcopy
import sys
input = sys.stdin.readline
n = int(input())
candy = []
answer = 0
for i in range(n):
    candy.append(list(input().rstrip()))

def getMaxCandyLen(new_candy):
    max_count = 0
    # n대신 len(new_candy)
    for i in range(n):
        for j in range(n):
            # 가로
            if j != n-1:
                count = 1
                for k in range(j+1,n):
                    if new_candy[i][j] == new_candy[i][k]:
                        count += 1
                    else:
                        max_count = max(max_count, count)
                        break
                max_count = max(max_count, count) # 끝나고 또 해주는 것이 꼭 이렇게 코드 짤 수 밖에 없나...
                
            # 세로
            if i != n-1:
                count = 1
                for k in range(i+1,n):
                    if new_candy[i][j] == new_candy[k][j]:
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
            new_candy = deepcopy(candy)
            temp = new_candy[i][j] 
            new_candy[i][j] = new_candy[i][j+1]
            new_candy[i][j+1] = temp
            answer = max(answer, getMaxCandyLen(new_candy))
        # 아래와 변경
        if i != n-1:
            new_candy = deepcopy(candy)
            temp = new_candy[i][j] 
            new_candy[i][j] = new_candy[i+1][j]
            new_candy[i+1][j] = temp
            answer = max(answer, getMaxCandyLen(new_candy))
            
print(answer)

# 전역변수로 둬서 함수에서 쓸 수 없을까?
# 처음엔 아래, 위, 옆을 나눠서 진행함. 생각해보다 오른쪽과 아래만 하면 된다. 

# 스트링 입력 개행문자 제거하려면 rstrip 써야함.

# n-1 에서 n으로 바꿈. 