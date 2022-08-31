# 듣보잡 (1764)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
see = []
answer = []

def binary(start, end, value):
    # see[(start + end) // 2] 가 mid. 중간점이다.
    mid = see[(start + end) // 2]
    if start > end:
        return False
    if mid == value:
        return True
    else:
        compare_range = int((start + end) // 2)
        if mid <= value:
            # compare_range 2, 2,3 => see[2] 값과 비교 (13Line)
            return binary(compare_range+1, end, value)
        else:
            return binary(start, compare_range-1, value)

for i in range(n):
    see.append(input().rstrip())
see.sort()

# 이진탐색
for _ in range(m):
    temp = input().rstrip()
    if(binary(0, m-1, temp)):
        answer.append(temp)
    else:
        continue
print(len(answer))
answer.sort() # 이 sort 때문에 시간을 많이 허비함.
for v in answer:
    print(v)

### 세윤이 보고 바꾼 코드 index 대신 in 활용
### 시간 초과
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# see = []
# answer = []

# for _ in range(n):
#     see.append(input().rstrip())

# for _ in range(m):
#     temp = input().rstrip()
#     if temp in see:
#         answer.append(temp)
# print(len(answer))
# answer.sort()
# for v in answer:
#     print(v)


### 1번째 코드
# for _ in range(n):
#     see.append(input().rstrip())

# for _ in range(m):
#     temp = input().rstrip()
#     try:
#         if see.index(temp) != -1:
#             answer.append(temp)
#     except ValueError:
#         continue

### 리뷰 
# 순차탐색 말고, 이진탐색으로 구현
# 18퍼에서 게속 해결 안됨.... => print하기 전 sort 할 것.

### 이진탐색
# 1. 소수점 제거 (int) 함수 활용
# 2. 중간점은 다 빼고 생각. +1(start), -1(end)


