# 쉬운 계단 수 (10844)
# 정답여부 : X
# 소요시간 : 분 (16:38 ~)

N = int(input())

dp = [[0]*10 for _ in range(N+1)]
# for i in range(1, 10):
#     dp[1][i] = 1
dp[1] = [0,1,1,1,1,1,1,1,1,1]
MOD = 1000000000

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 
print(sum(dp[N]) % MOD)

# 해결팁
# 1) dp[0]이 처음 오는 숫자이고, 
# dp[1]에서의 [0]은 dp[0][1] 에서 오는 경우만 존재한다. dp[0][-1]는 없으니까
# 즉, dp[n][0] = dp[n-1][1] 이라는 점
# 2) 그 외 dp[n][1~8]은 dp[n-1]에서 자신보다 한칸 작거나 큰 수의 값을 더한 값이다. 
# ex. dp[n][5] = dp[n-1][4] + dp[n-1][6]
# 3) 마지막으로 dp[n][9]도 dp[n-1][8]만 가능. 

# 헤맨점
# DP 문제임을 알았음에도 어떻게 해결하는지 몰랐다. 
# 좀 더 연구하고 풀어봐야할 듯 싶다. 
# 특히 초기값을 dp[1] = [0,1,1,1 ... 1]로 두는 것이 중요한 포인트 같다.