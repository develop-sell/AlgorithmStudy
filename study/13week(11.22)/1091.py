# 1091 

'''
6:48~ 7:13 못품
-< 0 1 2 0 1 2이기에. 
-> 각자 배열로 되어있지 않을까. 

1:10-1:24 다시 고쳐서 풀었다.

0,1,2
N개 카드. 
012 345

되돌아오면 어차피 안되는 식이지 않을까?


'''

n = int(input())
P = list(map(int, input().split())) # 정답
S = list(map(int, input().split()))

ans = [[] for _ in range(3)]
for i in range(n):
    ans[P[i]].append(i)

# print(ans)
change = [k for k in range(n)]
cnt = 0
exit = False
first = True
while not exit:
    
    # 첫번째 로직 제외
    # 탈출 구문1: 다시 원래 식으로 돌아오면 해당사항 없음 
    if first:
        first = False
    else:
        
        if change == [k for k in range(n)]:
            cnt = -1
            break
    exit = True
    
    
    # 탈출 구문2: 하나라도 안 맞으면 exit=False
    for l in range(n):
        if change[l] not in ans[l % 3]:
            exit = False
            break
            
    if exit:
        break
    
    
    # 횟수 + 1         
    cnt += 1
    
    
    # 값 변경 
    new_change = [0] * n
    for j in range(n):
        new_change[S[j]] = change[j]
    change = new_change
    

print(cnt)
    

