# 지능형 기차 2 (2460)
# 정답여부 : O
# 소요시간 : 10분 (10:23 ~ 10:33)

max = 0
current = 0
for i in range(10):
    getOut, getIn = map(int, input().split())
    current = current + getIn - getOut
    if max < current:
        max = current
print(max)

# 리뷰

# 헤맨점
# 1. input를 받고 숫자로 변경하는 식
#  -> map(int, input()) 까먹지말자!

# 풀이 2

