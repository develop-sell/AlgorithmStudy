# 1번째 방법
# backjoon(char)를 for문 돌면서 ord로 숫자로 만들고
# 숫자에 해당되는 index에 값을 더한다. (기본 -1 26개 만들어놓고.)

char = input()
answer = [-1] * 26
for i,v in enumerate(char):
    if answer[ord(v) - 97] == -1:
        answer[ord(v) - 97] = i

for v in answer:
    print(v, end=" ")
    

# 2번째 방법
# 알파벳을 for문 돌리면서, 알파벳이 word 안에 있는지 확인
# 있으면 해당 index 위치 값을. 아니면 -1를 출력 
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x))) 