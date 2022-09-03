# 1157 (단어 공부)

### 세번째 코드 (추천)
# 알파벳 26개를 순회하며 word에 빈도수를 count함수로 찾는다. 
# 최대로 사용된 수(n)과 비교하여 ?, 알파벳으로 c 값을 결정한다.
## => python은 함수 내에 있는 변수만 지역변수로 취급하고, 그 외 모두 전역변수 취급
## 예제에서 c 변수가 for문 안에 선언되어있지만, 전역변수로 취급
word=input().upper()
n=0 # 최대로 사용된 알파벳 수
for p in map(chr,range(65,91)):
    q=word.count(p)
    if n<q:
        # c: 최대로 사용된 알파벳
        n,c=q,p
    elif n==q:
        # 최대가 같은 알파벳이 있다면 ?, 그 보다 큰 값이 존재하면 다시 c는 알파벳으로
        c="?"
print(c)

#--------------------------------------------------------------------
### 두번째 코드 (1번째 코드 간결하게 변경)
# 여전히 update, max 함수 때문에 속도가 느리다.
word = input().rstrip().upper()
dc = dict()
max_count = 0
for v in word:
    if v in dc:
        max_count = max(max_count, dc.get(v) + 1)
        dc.update({v: dc.get(v) + 1})
    else:
        max_count = max(max_count, 1)
        dc.update({v: 1})

word_list = [k for k,v in dc.items() if v == max_count]
if len(word_list) > 1:
    print("?")
else:
    print(word_list[0])
    

#--------------------------------------------------------------------
### 첫번째 코드
# dictionary를 활용하여 각 문자별 빈도수를 key,value 형태로 저장한다
# 그 후 가장 많은 값을 가진 word_list를 만들고 
# 이때 word_list의 길이가 1 이상이면 ?를, 아니면 문자를 출력한다. 
# 아쉬운점: input부터 upper로 받으면 통일화되어 코드가 더 간결했을 것이다. 

import sys
input = sys.stdin.readline
word = input().rstrip()
dc = dict()
max_count = 0
for v in word:
    if 97 <= ord(v):
        v = chr(ord(v) - 32)
    if v in dc:
        max_count = max(max_count, dc.get(v) + 1)
        dc.update({v: dc.get(v) + 1})
    else:
        max_count = max(max_count, 1)
        dc.update({v: 1})

word_list = [k for k,v in dc.items() if v == max_count]
if len(word_list) > 1:
    print("?")
else:
    if 97 <= ord(word_list[0]):
        print(chr(ord(word_list[0]) - 32))
    else:
        print(word_list[0])