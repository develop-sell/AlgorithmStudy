### 리스트 컴프리헨션 : 1 ~ 7까지 숫자 중, 짝수들을 곱하기 4한, 값들을 모아둔 리스트
calculated_list = [n * 4 for n in range(1,8) if n % 2 == 0]

#-----------------------------------------------------------------------------------------#
### input: list로 변경하기 (-> [1,2,3])
# scores = list(map(int, input().split()))

#-----------------------------------------------------------------------------------------#
### 0 제외 최소값 구하기 #filter , #lambda, #map
### BOJ 9440 # 2022.08.08
# https://wikidocs.net/64
numbers = [0,1,2,3]
print(min(filter(lambda x: x > 0, numbers))) # --> [1,2,3] --> 1
print(map(lambda x: x > 0, numbers)) # --> [False, True, True, True]

#-----------------------------------------------------------------------------------------#
### reduce: 누적적으로 함수에 적용시키는.
from functools import reduce
print(reduce(lambda x, y: x + y, [1, 3, 5, 7]))
print(reduce(lambda x, y: y + x, 'abcde')) # 반대. #'edcba'
# 1회차: x=1, y=3 -> 1+3 = 4
# 2회차: x=4, y=5 -> 4+5 = 9
# 3회차: x=9, y=7 -> 9+7 = 16 # 정답은 16

#-----------------------------------------------------------------------------------------#
# count: 그 안의 갯수 세기
arr = ['s','e','i','l','l']
print(arr.count('s')) # 2

#-----------------------------------------------------------------------------------------#
### index: 맞는 문자 찾기. (find도 있지만, 문자열에서만 사용 가능)
a = [1,2,3,4,5]
try:
    print(a.index(10))
except ValueError:
    print("10 is not in list")

str = 'seil'
print(str.find('s')) # 0
print(str.find('a')) # -1 

#-----------------------------------------------------------------------------------------#
### 문자열 대비: 공백지우기
str = ' s e i l '
str.lstrip() # 왼쪽만
str.rstrip() # 우측만
str.strip() # 양쪽

#-----------------------------------------------------------------------------------------#
### 문자열 바꾸기 (문자열 안의 단어 자체를 변경)
a = 'seil house' 
a.replace("seil", "ham") # 'ham house' 

#-----------------------------------------------------------------------------------------#
### sort
l = [10,5,4,3,7,6]
k = [10,5,4,3,7,6]
l.sort()
sorted(k)
print(l, k)
# sorted(testCaseThree, key=lambda x: x[1]) # 뒤의 숫자 순서대로 정렬

#-----------------------------------------------------------------------------------------#
### 중복제거, 기존 리스트 순서 유지하면서 
array = ['1','3','5','1','4']
result = list(dict.fromkeys(array)) 

#-----------------------------------------------------------------------------------------#
### 문자열 대소 관계 (사전순으로 가능)
a = 'abc'
b = 'abcd'
c = 'abd'
print(a<b)
print(a<c)

#-----------------------------------------------------------------------------------------#
### 평균 -> 더 좋은 방법 있을 수도.
sample = [1,2,3]
average = sum(sample) / len(sample)

#-----------------------------------------------------------------------------------------#
### 문자열: 숫자로 된 문자열 각 자리수 더하기. 
num = '123'
print(sum([int(i) for i in num])) # 6 출력

#-----------------------------------------------------------------------------------------#
### 이진법 
num = 5
print(bin(num)) # 출력: 0b101 (0b는 binary를 표시하는 방식.)
print(bin(num).count('1')) # 2 


#-----------------------------------------------------------------------------------------#
### 전역변수 함수 내에서 사용법 global
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x) # fantastic으로 변경되어 출력

## => python은 함수 내에 있는 변수만 지역변수로 취급하고, 그 외 모두 전역변수 취급
## 예제에서 c 변수가 for문 안에 선언되어있지만, 전역변수로 취급
for i in range(3):
    global_num = i
print(global_num)

#-----------------------------------------------------------------------------------------#
### 큐, 스택
from collections import deque
queue = deque()

queue.append(5)
queue.append(2)
queue.popleft()
queue.append(7)

queue.reverse() # 역순으로 바꾸기 
print(queue) # 나중에 들어온 원소부터 출력 [7,2] (오른쪽부터 나가는 queue)

### 스택 
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()

print(stack[::-1]) # 거꾸로 출력 [2,1] (왼쪽부터 나가는 stack)

#-----------------------------------------------------------------------------------------#
### 두번째로 큰 수 찾기
# https://shoark7.github.io/programming/algorithm/second-largest-number-in-array
def second_largest_number(arr):
    second = largest = -float('inf') 
    
    for n in arr:
        if n > largest:
            second = largest
            largest = n
        elif second < n < largest:
            second = n

    return second