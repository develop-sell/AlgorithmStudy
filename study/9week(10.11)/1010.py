# 다리 놓기 (1010)
# 6:02-6:18
# 단 다리가 서로 겹칠 수 없다는 점.
# 조합으로 문제 풀기. 
# nCr -> n! / r! * (n-r)!
import sys, math
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    n, m = map(int, input().split())
    ans = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
    if n == 0:
        print(0)
    else:
        print(int(ans))
# import sys
# input = sys.stdin.readline
# n = int(input())
# for _ in range(n):
#     n, m = map(int, input().split())
#     ans = 1
#     for i in range(m, m-n,-1):
#         ans *= i
#         ans //= (n-(m-i))
#     if n == 0:
#         print(0)
#     else:
#         print(int(ans))

# import sys
# input = sys.stdin.readline
# n = int(input())
# for _ in range(n):
#     n, m = map(int, input().split())
#     ans = 1
#     for i in range(m, m-n,-1):
#         ans *= i
#     for i in range(n,0,-1):
#         ans /= i
#     if n == 0:
#         print(0)
#     else:
#         print(int(ans))