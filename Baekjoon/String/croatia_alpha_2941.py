### 크로아티아 알파벳 (2941)
## 7:35 - 7:52
## 기준을 다르게 잡아볼 필요가 있다. 

# 더 좋은 코드 - 마스킹 전략.

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 반드시 dz=가 z=보다 앞에 있어야한다.
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))

# 1번째 코드
# n = input() # dz= lj es=njak # 7
# arr = ["c=", "c-", "lj", "nj", "s=", "z=", "dz=", "d-"]
# count = 0
# pass_count = 0
# for i in range(len(n)):
#     if pass_count > 0:
#         pass_count += -1
#         continue
#     if i == len(n) - 1:
#         count += 1
#         continue
#     if n[i] == "c" and (n[i+1] == "=" or n[i+1] == "-"):
#         count += 1
#         pass_count += 1
#     elif n[i] == "l" and n[i+1] == "j":
#         count += 1
#         pass_count += 1
#     elif n[i] == "n" and n[i+1] == "j":
#         count += 1
#         pass_count += 1
#     elif n[i] == "s" and n[i+1] == "=":
#         count += 1
#         pass_count += 1
#     elif n[i] == "z" and n[i+1] == "=":
#         count += 1
#         pass_count += 1
#     elif n[i] == "d" and n[i+1] == "-":
#         count += 1
#         pass_count += 1
#     elif i != len(n) -2 and n[i] == "d" and n[i+1] == "z" and n[i+2] == "=":
#         count += 1
#         pass_count += 2
#     else:
#         count+=1

# print(count)