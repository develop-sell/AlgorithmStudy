# 듣보잡 (1764)
# 10:10
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 사전순 
see = []
answer = []

def findTree(start, end, value):
    # see[(start + end) // 2] 가 mid. 중간점이다.
    if start > end:
        return False
    if see[(start + end) // 2] == value:
        return True
    else:
        compare_range = int((start + end) // 2)
        if see[compare_range] <= value:
            # compare_range 2, 2,3 => see[2] 값과 비교 (13Line)
            return findTree(compare_range+1, end, value)
        else:
            return findTree(start, compare_range-1, value)

for i in range(n):
    temp1 = input().rstrip()
    see.append(temp1)
see.sort()

# tree로 탐색
for _ in range(m):
    temp = input().rstrip()
    if(findTree(0, m-1, temp)):
        answer.append(temp)
    else:
        continue
print(len(answer))
answer.sort() # 이 sort 때문에 시간을 많이 허비함.
for v in answer:
    print(v)


# for _ in range(n):
#     see.append(input().rstrip())

# for _ in range(m):
#     temp = input().rstrip()
#     try:
#         if see.index(temp) != -1:
#             answer.append(temp)
#     except ValueError:
#         continue



# 순차탐색 말고. 이진탐색으로 구현
# 18퍼에서 게속 해결 안됨.... => sort 문제.
## 이진탐색
# 1. 소수점 제거 (int) 함수 활용
# 2. 중간점은 다 빼고 생각. +1(start), -1(end)