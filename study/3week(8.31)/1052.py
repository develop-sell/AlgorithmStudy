# 1052 물병
# 해결 X -> 12:05 ~ (시간초과)

n, k = map(int, input().split())

addtional_bottle_cnt = 0

while bin(n).count('1') > k:
    # 1. 이진법 변경 -> 2. 뒤에서부터 1를 가진 index
    # ex. 10 -> 1010 -> idx는 1임. 
    # ex. 12 -> 1100 -> idx는 2임. 
    idx = bin(n)[::-1].index('1') 
    addtional_bottle_cnt += 2**idx # 2^n를 더한다.
    n += 2**idx

print(addtional_bottle_cnt)


# 1번째 풀이 (시간초과)
# n, k = map(int, input().split())

# bottles = n * [1] # 계속 변경
# purchase = 0
# while len(bottles) > k:
#     new_bottles = []
#     is_merged = False # 
#     merge_num = False # 이미 merge한 i+1 숫자를 패스하기 위한 변수
#     for i in range(len(bottles)-1):
#         if merge_num:
#             merge_num = False
#             continue
#         if bottles[i] == bottles[i+1]:
#             # 이 경우 합치기
#             new_bottles.append(bottles[i] + bottles[i+1])
#             merge_num = True
#             is_merged = True
#         else:
#             new_bottles.append(bottles[i])
    
#     if merge_num == False:    
#         # 마지막 숫자의 경우, merge숫자가 아니면 추가해준다. 
#         # => 위 for문이 n-1까지라서. 
#         new_bottles.append(bottles[len(bottles)-1])        
#     if is_merged == False:
#         # 한번도 merge 하지 못했으면 새로운 병 추가.
#         new_bottles.append(1)
#         purchase += 1
#     bottles = new_bottles

# print(purchase)