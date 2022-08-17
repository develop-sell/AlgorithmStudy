# 빙고 (2578)
# 정답여부 : O
# 소요시간 : 1시간 34분 (12:56 ~ 2:30) 
# study(1week)
def delete_and_check_line(num):
    additional_bingo = 0
    row = -1
    column = -1
    for i in range(5):
        for j in range(5):
            
            if arr[i][j] == num:
                arr[i][j] = -1
                row = i
                column = j
                # 이중 for문을 두번 빠져나오는 방법이 없을까?
                break
        if row != -1 and column != -1:
            break
    if arr[row] == [-1,-1,-1,-1,-1]:
        # 가로
        additional_bingo = additional_bingo + 1
    if arr[0][column] == -1 and arr[1][column] == -1 and arr[2][column] == -1 and arr[3][column] == -1 and arr[4][column] == -1:
        # 세로
        additional_bingo = additional_bingo + 1
    # 우상향대각선
    if row + column == 4:
        # 검색 순서: (4,0), (3,1), (2,2), (1,3), (0,4)
        is_bingo = True
        for k in range(5):
            if arr[4 - k][k] == -1:
                continue
            else:
                is_bingo = False
                break
        if is_bingo:
            additional_bingo = additional_bingo + 1
    # 우하향대각선
    if row == column:
        # 검색순서: (4,4), (3,3), (2,2), (1,1), (0,0)
        is_bingo = True
        for k in range(5):
            if arr[4 - k][4 - k] == -1:
                continue
            else:
                is_bingo = False
                break
        if is_bingo:
            additional_bingo = additional_bingo + 1
    
    return additional_bingo
    

count = 0
bingo = 0
arr = []
        
for i in range(5):
    arr.append(list(map(int, input().split())))

for i in range(5):
    for j, v in enumerate(list(map(int, input().split()))):
        # 한번에 4가 되는 경우도 존재. (맨마지막으로 가운데 설정되면)
        if bingo >= 3:
            break
        count = count + 1
        bingo = bingo + delete_and_check_line(v)
    
    if bingo >= 3:
        break
print(count)


# 한번에 4가 되는 예외 케이스

# i, j = row + (4 - row), column - (4 - row)
# if i == 4 and j == 0:

# i, j = row + (4 - row), column + (4 - row)
# if i == 4 and j == 4:

# - 단, 대각선은 대각선 위치에 존재할 때만 확인.
# - 대각선 위치는 2가지 case
#     1. 우상향 (row + column = 4) ⇒ ex. (3,1), (4,0)
#     2. 우하향 (row -  column = 0) ⇒ ex. (3,3), (0,0)