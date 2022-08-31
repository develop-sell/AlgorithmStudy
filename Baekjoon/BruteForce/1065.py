# 1065 (한수)
# 3:55~4:06

import sys
input = sys.stdin.readline
n = int(input())

answer = 0
for i in range(1, n+1):
    # 간격이 다 같은지. 체크
    interval = 0
    num_list = [int(j) for j in str(i)]
    # 1자리 수는 패스 => 2자리까지도 패스 가능.
    if len(num_list) == 1:
        answer += 1
        continue
    interval = num_list[0] - num_list[1]
    is_han_num = True
    for k in range(len(num_list) - 1):
        if interval != num_list[k] - num_list[k+1]:
            is_han_num = False
            break
    
    if is_han_num:
        answer += 1

print(answer)