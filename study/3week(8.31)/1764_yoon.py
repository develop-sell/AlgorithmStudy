### 김윤현
### set함수, 교집합으로 문제 해결
import sys 

input = sys.stdin.readline

n,k = map(int, input().split())
no_listen = set()
no_see = set()

for i in range(n):
    no_listen.add(input().rstrip())

for i in range(k):
    no_see.add(input().rstrip())

no_see_listen = no_listen & no_see # 교집합

print(len(no_see_listen))
for nsl in sorted(no_see_listen):
    print(nsl)