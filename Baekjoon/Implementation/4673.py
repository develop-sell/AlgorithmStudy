# 셀프넘버 (4673)
# 3:20 ~ 3:30

# 첫번째 코드. 대신 느리다 584ms -> index 함수를 10000번 사용해서 인 듯.
found = []

for i in range(1, 10001):
    try:
        found.index(i)
    except:
        print(i)
    num = i + sum([int(i) for i in str(i)])
    found.append(num)

# 두번째 코드 (참고)
nn = set(range(1, 10001)) # 전체
gn = set() # 담을 공간

for i in range(1, 10001):
    num = i + sum([int(i) for i in str(i)])
    gn.add(num)

sn = sorted(nn - gn)
for i in sn:
    print(i)  
