
# A = [1,3,6,4,1,2]
A = [1,2,3]
# A = [-1,-3]
A_set = set(A)
# 마이너스 숫자들 삭제. => 이게 성능 떨구는 듯. (for문을 2번 돌리기에) 
A_set = [0] + [ele for ele in A_set if ele > 0]

if len(A_set) == 1:
    print("1")

is_pass = True
i = 0
while is_pass:
    i = i + 1
    if len(A_set) <= i or A_set[i] != i:
        is_pass = False

print(i)
    
    
    

# def solution(A):
#     # write your code in Python 3.6
#     A_set = set(A)
#     A_set = [0] + [ele for ele in A_set if ele > 0]

#     if len(A_set) == 1:
#         return 1

#     is_pass = True
#     i = 0
#     while is_pass:
#         i = i + 1
#         if len(A_set) <= i or A_set[i] != i:
#             is_pass = False

#     return i