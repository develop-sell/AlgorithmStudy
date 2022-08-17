# 병사 배치하기 (18353)
# 정답여부 : X
# 소요시간 : 2:54 ~ 못 품. 


n = int(input())
power =list(map(int,input().split()))
dp = [1] * n # 처음부터 1이기에.
for i in range(1, n):
    for j in range(i): ### for문의 끝이 i라는 점. 
        if power[j]>power[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))


# bottom 방식 말고.. top으로? 
# 1개가 추가되면 어떻게 되는건지?

### 예외케이스
# case 1
# => 2(11, 4)
# 7 
# 15 11 4 8 5 2 4
# case 2
# => 2(11, 4)
# 10 
# 15 11 4 14 13 12 11 10 9 8
# case 3
# => 1(14)
# 4 
# 15 11 4 14 
# case 4
# => 3(11,4,9)
# 7 
# 15 11 4 14 10 9 9
# case 5
# => 2(4,14) 
# 8 
# 15 11 4 14 10 9 2 1


# start = time.time()  # 시작 시간 저장
# print("time: ", (time.time() - start) * 10000 )  # 시작 시간 저장

# 같은 전투력도 우선 제외 (무조건 높아야하기때문)
# 여기서 이렇게 되는 경우 j-1이 아닌 j-2와 비교해야한다. 
# 15 17 16 18 이 경우. 16이 용인된다. 
        
# out_counts = [0] * n # 열외 숫자
# out_counts는 따로 필요 없다. 최대값을 n에서 빼면 되니까. 

#-----
# dp 안에 dp?? 
# 5 2 4면 그 중 어떤 것이 최대값인지.?
# 이것이 그 이후의 값들에서도 최대값일까? 
# 

#------------------------------------------------------
### 처음 짠 코드
# n = int(input())
# soldiers = list(map(int, input().split()))
# dp = [0] * (n-1) # 남은 병사(최대값 찾기


# def f(i):
#     if dp[i] != 0:
#         return dp[i]
    
#     if soldiers[i] > max(soldiers[i+1:]):
#         return f(i+1) + 1
#     else:
#         # 첫 수부터 작은 경우. 
#         return max(f(i+1), f(i+2))
    
# if soldiers[n-2] < soldiers[n-1]:
#     dp.append(1)
# else:
#     dp.append(2)    
# for i in range(n-3, -1, -1):
#     dp[i] = f(i)        

# print(dp[1])

#------------------------------------------------------
### 2번째 짠 코드
# n = int(input())
# soldiers = list(map(int, input().split()))
# dp = [0] * (n-1) # 남은 병사(최대값 찾기)
# dp.append(1)


# def f(i):
#     if dp[i] != 0:
#         return dp[i]
    
#     if soldiers[i-1] > soldiers[i]:
#         return f(i+1) + 1
#     else:
#         return max(f(i+1), f(i+2))

# print(n - f(1))

#------------------------------------------------------
### 3번째 풀이
# n = int(input())
# soldiers = list(map(int, input().split()))
# dp = [0] * n # 남은 병사(최대값 찾기)
# sub = -1
# if soldiers[0] > soldiers[1]:
#     sub = 2
# else:
#     sub = 1
# dp[0] = 1
# dp[1] = sub

# for i in range(2,n-1):
#     if soldiers[i-1] > soldiers[i]:
#         dp[i] = dp[i-1] + 1
#     else:
#         dp[i] = max(dp[i-1], dp[i-2])
        
# print(n - dp[n-2])