# 두 수의 합 (3273)
# 정답여부 : O
# 소요시간 : 1시간 5분 (11: 05 ~ 12:10)
answer = 0
count = int(input())
arr = list(map(int, input().split()))
num = int(input())
arr.sort()
j = len(arr) - 1
i = 0
while i < j:
    # i, j는 포인터
    if arr[i] + arr[j] > num:
        j = j - 1
    elif arr[i] + arr[j] < num:
        i = i + 1
    else:
        answer = answer + 1
        i = i + 1
        j = j - 1
print(answer)

# 풀이 리뷰
# i는 처음부터, j는 끝부터 온다
# 배열이 1,2,3,4,5 라고 하고. num 값이 6이라고 했을 때. 
# (1,5)가 되고나서 (2,5) 혹은 (1,4)는 절대 될 수 없어서 
# i도 +1, j도 -1 하도록 한다. 즉 (2,4) 부터 계산하도록. 


# 헤맨점
# 1번째. 점화식 DP문제로 착각. 
# 절반씩 나눠서? f(1,3) = f(1,2) + f(2,3) -> 이건 점화식. Dp 문제인데. 
# f(1,5) = f(1,3) + f(3,5)
# -> 이건 아닌게. 1번째 + 7번째를 해결하지 못함. 
# 26,27줄 설명 부분을 깨닫지 못하고, 이중 포문으로 돌리고 있었다. 
# 투포인터 문제는 while문으로 풀어보자.


### 첫번째 풀이. 브루스포스 방식 (시간 초과)
# answer = 0
# count = int(input())
# arr = list(map(int, input().split()))
# num = int(input())
# arr.sort()
# for i in range(len(arr)):
#     for j in range(len(arr)-1, i, -1):
#         # i, j는 포인터
#         if arr[i] + arr[j] > num:
#             continue
#         elif arr[i] + arr[j] < num:
#             #dd
#             break
#         else:
#             answer = answer + 1
# print(answer)


# range 거꾸로 가는 방법
# for j in range(7, -1, -2):
#     # i, j는 포인터
#     print(j)
