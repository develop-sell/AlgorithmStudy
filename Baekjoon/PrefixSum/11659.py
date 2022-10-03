# 11659 (구간합 구하기 4)

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0]
val = 0
for v in arr:
    val += v
    prefix_sum.append(val)
for i in range(m):
    s,e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])