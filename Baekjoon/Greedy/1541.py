# 1541 (잃어버린 괄호)
# 4:20-4:50
# 최소값 찾기.

# 55-50+40 => 55-(50+40) = -35
# 55-50-40+20 
# - 나오는 기점으로 뒤에 다 계산한 값의 최소값 찾기
# 55-50-40+20-20
# -면 뒤에 +까지는 다 합해서 하는것?

# 두번째 코드 
# - 기준으로 나누고, 다음 - 전까지의 숫자를 다 더해서 빼준다. 
# 단, 첫번째 숫자만 더해준다.

formula = input().split("-")

ans = sum(map(int, formula[0].split("+")))

for i in range(1, len(formula)):
    ans -= sum(map(int, formula[i].split("+")))

print(ans)


### 첫번째 코드
# 모든 경우 수를 고려해서 코드 구현
# 너무 복잡하게 생각함. 
# n = input() + "="
# formula = []
# cur = ''
# for v in n:
#     if v.isdigit():
#         cur += v
#     else:
#         formula.append(cur)
#         cur = ''
#         if v != "=":
#             formula.append(v)

# ans = 0 
# minus_cur = 0 
# minus_flag = False
# pass_cnt = 0
# for i in range(len(formula)):
#     if pass_cnt > 0:
#         pass_cnt += -1
#         continue  
#     if formula[i].isdigit():
#         # 숫자면(첫번째 경우만)
#         if minus_flag:
#             minus_cur += int(formula[i])
#         else:
#             ans += int(formula[i])
#     else:
#         # 숫자가 아니면
#         if minus_flag:
#             if formula[i] == "-":
#                 # 빠져나오자.
#                 ans += -minus_cur
#                 minus_cur = 0
#                 pass_cnt += 1
#                 minus_cur += int(formula[i+1])
#             else:
#                 pass_cnt += 1
#                 minus_cur += int(formula[i+1])
#         else:
#             if formula[i] == "-":
#                 minus_flag = True
#                 pass_cnt += 1
#                 minus_cur += int(formula[i+1])
#             else:
#                 pass_cnt += 1
#                 ans += int(formula[i+1])
# ans += -minus_cur
# print(ans)