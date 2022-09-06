# 게으른 백곰 (10025)
# 5:54 ~ 시간초과...흠.
# else문 쪽을 다른 방식으로 진행해야 할 듯.
# import time
import sys
input = sys.stdin.readline

# start = time.time()
n, k = map(int, input().split())
ans = 0

if k >= 500000:
    for i in range(n):
        g, x = map(int, input().split())
        ans += g
    
else:
    # 시작점은 0부터, 끝점 2k까지. max를 구한다. 
    ices = [0] * 1000001
    max_range = 0
    min_range = sys.maxsize
    for i in range(n):
        g, x = map(int, input().split())
        ices[x] = g
        max_range = max(max_range, x)
        min_range = min(min_range, x)
    # print("처음 for문 끝", time.time() - start)
    # 처음 sum 값. 
    ans = max(ans, sum(ices[min_range:2*k+min_range+1]))
    curr = ans
    for i in range(min_range, max_range - 2*k):
        # slice가 시간이 오래걸리나?
        if ices[i + 2*k+1] == 0:
            curr = curr - ices[i]
            continue
        else:
            curr = curr - ices[i] + ices[2*k+i+1]
            # current 값을... 
            ans = max(ans, curr)
print(ans)
# print("실행 끝", time.time() - start)

### 리뷰 
# 매번 slice 후 sum를 구하는 것 보다는 
# 하나씩 늘어나고 줄어드는 값들을 더하고 빼주는 로직이 더 맞다. 
# arr[1:101] == arr[0:100] - arr[0] + arr[101]

# 슬라이딩 윈도우 알고리즘(sliding window)
# 일정한 범위를 가지고 있는 것을 유지하며 이동하는 것
# 매번 처리되는 중복 요소를 버리지 않고 재사용함으로써
# 낭비되는 계산을 하지 않는 것.
# https://blog.fakecoding.com/archives/algorithm-slidingwindow 