# 시그널 (16113)
# 3:20~4:58


n = int(input())
codes = list(input())
start_points_numbers = [] # 0은 index, 1은 숫자.
# 40 / 5 => 8 
# 2n / 5
# 첫번째 줄 
count = 0
for i in range(n // 5):
    if count > 0:
        count = count - 1
        continue
    if codes[i] == '#':
        # 1과 그 외 다른 숫자인가 비교. 
        if codes[i + n//5] == '#' and codes[i + (2 * n) // 5] == '#' and codes[i + (3 * n) // 5] == '#' and codes[i + (4 * n) // 5] == '#' and codes[i+1] == '.':
            # 1 숫자:  일자 검정 & i+1은 검정이 아닌 숫자. 
            count = count + 1
            start_points_numbers.append((i, 1))
        elif codes[i + n//5] == '#' and codes[i + (2 * n) // 5] == '#' and codes[i + (3 * n) // 5] == '#' and codes[i + (4 * n) // 5] == '#' and i+1 == n//5:
            # 끝 수인 경우. 반례 1
            count = count + 1
            start_points_numbers.append((i, 1))
        else:
            # 다른 숫자: 4와 그 외 숫자.
            count = count + 3
            if codes[i+1] == '.' and codes[i+2] == '#':
                start_points_numbers.append((i, 4))
            else:
                start_points_numbers.append((i, 0))
# 두번째 줄
for i, v in enumerate(start_points_numbers):
    ## 1,4이면 안하도록 구현.
    if v[1] == 1 or v[1] == 4:
        continue 
    # 2,3,7
    if codes[v[0] + n // 5] == '.' and codes[v[0] + 1 + n // 5] == '.' and codes[v[0]+2 + n // 5] == '#':
        start_points_numbers[i] = (v[0], 2)
    # 5,6
    elif codes[v[0] + n // 5] == '#' and codes[v[0] + 1 + n // 5] == '.' and codes[v[0]+2 + n // 5] == '.':
        start_points_numbers[i] = (v[0], 5)
    # 8,9,0
    elif codes[v[0] + n // 5] == '#' and codes[v[0] + 1 + n // 5] == '.' and codes[v[0]+2 + n // 5] == '#':
        start_points_numbers[i] = (v[0], 8)

# 세번째 줄
for i, v in enumerate(start_points_numbers):
    ## 1,4이면 안하도록 구현.
    if v[1] == 1 or v[1] == 4:
        continue 
    # 7
    if v[1] == 2 and codes[v[0] + 2*n // 5] == '.' and codes[v[0] + 1 + 2*n // 5] == '.' and codes[v[0]+2 + 2*n // 5] == '#':
        start_points_numbers[i] = (v[0], 7)
    # 0
    elif v[1] == 8 and codes[v[0] + 2*n // 5] == '#' and codes[v[0] + 1 + 2*n // 5] == '.' and codes[v[0]+2 + 2*n // 5] == '#':
        start_points_numbers[i] = (v[0], 0)

# 네번째 줄
for i, v in enumerate(start_points_numbers):
    ## 1,4이면 안하도록 구현.
    if v[1] == 1 or v[1] == 4:
        continue 
    # 3
    if v[1] == 2 and codes[v[0] + 3*n // 5] == '.' and codes[v[0] + 1 + 3*n // 5] == '.' and codes[v[0]+2 + 3*n // 5] == '#':
        start_points_numbers[i] = (v[0], 3)
    # 6
    elif v[1] == 5 and codes[v[0] + 3*n // 5] == '#' and codes[v[0] + 1 + 3*n // 5] == '.' and codes[v[0]+2 + 3*n // 5] == '#':
        start_points_numbers[i] = (v[0], 6)
    # 9
    elif v[1] == 8 and codes[v[0] + 3*n // 5] == '.' and codes[v[0] + 1 + 3*n // 5] == '.' and codes[v[0]+2 + 3*n // 5] == '#':
        start_points_numbers[i] = (v[0], 9)

for i, v in enumerate(start_points_numbers):
    print(v[1], end='')


### 해결 방식.
# start_points와 number_list를 튜플로 만들어야할 듯. 

## 반례 1
# 25
# #...##...##...##...##...#
# 11 

## 반례 2
# 35
# #.#.####.#.#..###.###..#...#..#.###
# 45
# 첫번째 줄에 1,4를 구분짓는데 4를 if문에서 제외시켰다는 점
# 0대신 8로 조건 바꿨는데, v[1] == 0 을 그대로 뒀다는 점. 