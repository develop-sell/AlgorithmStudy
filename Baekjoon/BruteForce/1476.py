# 날짜 계산

E,S,M,ans =1,1,1,1

e,s,m = map(int,input().split())

while not(e==E and s==S and m==M):
    E+=1 ; S+=1 ; M+=1; ans+=1
    if E>=16 : E-=15
    if S>=29 : S-=28
    if M>=20 : M-=19

print(ans)