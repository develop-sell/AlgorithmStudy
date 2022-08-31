# 테이블의 크기가 50보다 작기 때문에 브루트포스로 풀 수 있음
# 인접한 두 칸을 고르고 사탕을 교환하는 방법은 상하좌우로 4가지가 있다. 
# 그러나 테이블을 순차적으로 검사했을때, 위로 바꾸는 방법과, 왼쪽으로 바꾸는 방법은 이전에 검사했었으므로 다시 고려할 필요가 없다.
# 그러므로 밑으로 바꾸는 방법과, 오른쪽으로 바꾸는 방법 두 가지만 고려하면 된다.

import sys
input=sys.stdin.readline

def check(n, arr):
    answer=1
    for i in range(n):
        # 열 순회하면서 연속되는 숫자 세기
        cnt=1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                # 이전 것과 같다면 +1
                cnt += 1
            else:
                # 이전과 다르면 1로 초기화
                cnt=1

            # 현재 cnt가 크다면 answer 갱신
            if cnt > answer:
                answer=cnt

        # 행 순회하면서 연속되는 숫자 세기
        cnt=1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                # 이전 것과 같다면 +1
                cnt += 1
            else:
                # 이전과 다르면 1로 초기화
                cnt=1

            # 현재 cnt가 크다면 answer 갱신
            if cnt > answer:
                answer=cnt

    return answer


n=int(input())
arr=[list(input().rstrip()) for _ in range(n)]
# print(arr)
answer=0

for i in range(n):
    for j in range(n):
        # 열 바꾸기
        if j < n-1:
            # 인접한 데이터와 바꾸기
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        
            # 가장 긴 부분을 check
            tmp=check(n, arr)

            if tmp > answer:
                answer=tmp

            # 원래대로 돌려놓기
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        
        # 행 바꾸기
        if i < n-1:
            # 인접한 데이터와 바꾸기
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
        
            # 가장 긴 부분을 check
            tmp=check(n, arr)

            if tmp > answer:
                answer=tmp

            # 원래대로 돌려놓기
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(answer)