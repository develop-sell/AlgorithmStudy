# 프로그래머스: 점 찍기(140107)
# 2:20 ~ 3:31

k = 1
d = 5

import math

ans = 0
for i in range(0,d//k+1):
    # 각 줄에 몇개의 정답이 있는지 
    ans += (int((math.sqrt(d**2 - (k*i)**2)) / k) + 1)
print(ans)


## 생각흐름 
'''
d(원점과의 거리)의 정의가 애매해서 헷갈렸다.
실제 직선거리를 말하는지, 아니면 가로세로 축의 합 거리를 말하는지. 

직선거리를 뜻하는 것이었고. 
한 줄마다 ans가 몇 개씩 있는지 확인해서 정답을 구했다. 
만약 한줄이 접근하면 시간초과가 날 것이다. (제한사항이 100만이기에 100만*100만은 1억)
직선거리 값 = math.sqrt((k*i)**2 + (k*x)**2)) -> i번째이기에 세로길이는 k*i이고, 가로는 x(미지수)*k이다. 
그리고 이 직선거리가 d보다 작을 때까지의 값을 고려하는 것. 

따라서 "직선거리 < d" 이렇게 식을 두고. 하나씩 풀면 x의 범위가 나온다. 
'''



## 1번째 풀이 
# 가로세로합이 원점과의 거리라고 착각했을 때의 식
'''
ans = 0
for i in range(1,(d//k) + 2):
    ans += i
print(ans)
'''