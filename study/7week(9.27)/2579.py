# 2579 (계단오르기)
# 12:13 ~ 12:57

# dp = 각 계단의 최대치. 

n = int(input())
dp = [0] * (n+1)
dp[1] = int(input())

is_con = False
before = 0
for i in range(2, n+1):
    now = int(input())
    if is_con:
        if dp[i-3] + before + now > dp[i-2] + now:
            dp[i] = dp[i-3] + before + now
            is_con = True
        else:
            dp[i] = dp[i-2]+now
            is_con = False
    else:
        if dp[i-1]+now > dp[i-2]+now:
            dp[i] = dp[i-1]+now
            is_con = True
        else:
            dp[i] = dp[i-2]+now
            is_con = False
    before = now
print(dp[n])


# 반례 1
# 3
# 10
# 20
# 40
# 정답: 60

# i-3까지 고려하는 것이 중요.