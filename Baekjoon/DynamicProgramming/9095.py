# 1,2,3 더하기 (9095)
# 정답여부 : X
# 소요시간 : 40분 (16:20 ~ 16:58)

count = int(input())

def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sol(n-1) + sol(n-2) + sol(n-3)

for i in range(count):
    n = int(input())
    print(sol(n))

# 리뷰
# 모든 예시를 제대로 못 잡은 점이 컸다. 점화식인 것은 알았지만 규칙을 못 찾은 점. 
# 더 꼼꼼하게 볼 필요가 있다. 

# 헤맨점
# f(n) = f(n-1) + f(n-2) + f(n-3) 를 생각 못하고 있었다.
# 생각했다면 금방 보이지 않았을까... 
# def로 함수로 만들어서 하는 방식이 훨씬 보기 깔끔하다. 

# 처음 풀이
count = int(input())
list = []
for i in range(count):
    list.append(int(input()))

for i in range(count):
    n = list[i]
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 4:
        print(3)
    else:
        dp = [1,2,4]
        dp = dp + [1] * (n - 2)
        for j in range(2, n+1):
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
        print(dp[n-1])