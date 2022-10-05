# 패션왕 신해빈 (9375)
# 5:48 - 6:00
import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    dict = {}
    for _ in range(int(input())):
        name, cate = input().split()
        if cate not in dict:
            dict[cate] = [name]
        else:
            dict[cate].append(name)
    
    ans = 1
    for key in dict:
        ans *= (len(dict[key])+1)
    
    # 3*2-1 = 5 (경우의수 문제)
    print(ans - 1)