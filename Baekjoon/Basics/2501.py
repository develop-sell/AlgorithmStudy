# 약수 구하기 (2501)
# 정답여부 : O 
# 소요시간 : 15분 (09:47 ~ 10:02)

import math

N, index = map(int, input().split())
cnt = 0
for i in range(1, (N // 2) + 1):
    if (N % i == 0):
        cnt += 1
        if (cnt == index):
            print(i)
            break
if (cnt + 1 == index):
    print(N)
elif (cnt < index):
    print(0)


# 리뷰 
# 리스트를 만들어서 값들을 넣은 후, index에 해당하는 값을 꺼내려다가
# 불필요해보여서 한번 for문 돌면서 접근하는대로 print하도록 구현

# 헤맨점 
# 자기 자신을 약수로 두는 점을 예외처리 못했다. 
# 15번 줄 cnt+1 == index인 경우가 자기 자신인 경우이다. 

# 풀이 2 
# for i in range(1, math.ceil(math.sqrt(N)) + 1): 

# 이렇게 풀면, 조금 더 연산 시간을 줄일 수 있다. 
# N의 약수는 N^0.5의 올림까지만 적용해보면 된다. 
# math.ceil -> 올림 , math.sqrt -> 루트(^0.5) // import math 해야한다. 