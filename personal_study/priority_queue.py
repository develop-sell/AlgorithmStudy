'''
우선순위 큐는 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
ex. 가치가 높은 물건부터 꺼내서 확인하는 경우
ex. 10일전, 8일전 값 중 더 오래된 값을 꺼내는 경우

구현 방법
1) 단순히 리스트 이용해서 구현
2) 힙을 이용하여 구현


시간 복잡도
데이터 N개일 때, 
리스트는 삽입: O(1) , 삭제: O(N) 선형탐색
힙 삽입: O(logN),  삭제: O(logN) 

단순히 N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업은 정렬과 동일 (힙정렬)
O(NlogN)

힙의 특징
- 항상 루트노드를 제거 
- 완전이진트리
최소힙, 최대힙이 존재. 
최소힙: 루트 노드가 가장 작은 값 (가장 작은 값부터 삭제)
최대힙: 루트 노드가 가장 큰 값. (가장 큰 값부터 삭제)

데이터 삽입
계속 부모를 거슬러 올라가면서
자신보다 작은 값인지 비교해서 바꾼다. 
만약 큰 값이면 그 자리에서 스탑. 
ex. 깊이3인 노드에서 깊이 2인 노드와 비교.
만약 더 자신이 더 작으면 깊이 2 노드와 변경
그 다음 깊이 1과 비교. 만약 자신보다 크면 변경 x 

데이터 삭제 
마지막 노드를 루트노드로 이동 (루트노드 삭제)
다음 자식과 비교해서 더 작은 자식과 위치를 변경함

유의점
데이터를 삽입/삭제할 때마다 구조는 달라진다.
단 루트노드만은 무조건 최소값인 것. 
나머지 가지들은 순서는 따로 없다고 생각하자. 
(물론 자식들이 본인보다 크다는건 맞음.)
(대신 왼쪽 자식이 오른쪽 자식보다 더 크거나 그런건 없다)


파이썬의 경우 heapq 라이브러리 활용
또한 기본적으로 최소힙이다!!!! 

만약 최대힙으로 구성하고 싶으면 
데이터를 넣을 때와 데이터를 꺼낼 떄 (-) 를 붙이면 된다

'''

# 1 3 7 2 
# -> 1 2 7 3 
# 1은 루트노드, 2,7은 깊이1, 3은 깊이 2

import heapq

def heapsort(arrr):
    h = []
    result = []
    
    for value in arrr:
        # h라는 heap에 value를 넣는다.
        heapq.heappush(h, value)
    
    for i in range(len(h)):
        # h라는 heap에서 pop을 한다.
        result.append(heapq.heappop(h))
    
    return result

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n):
    print(res[i])