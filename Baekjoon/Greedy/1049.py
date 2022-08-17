# 기타줄 (1049)
# 정답여부 : O
# 소요시간 : 40분 (18:43 ~ 19:23)
# study(1week)

strings, m = map(int, input().split())
total = 0
bundles = []
pieces = []
for i in range(m):
    bundle, piece = map(int, input().split())
    bundles.append(bundle)
    pieces.append(piece)

remain_strings = 100000

if remain_strings > 6:
    total = min(bundles) * (strings // 6)
    remain_strings = strings - (strings // 6) * 6

if min(pieces) * remain_strings > min(bundles):
    # 3번 예제입력
    total = total + min(bundles)
else:
    total = total + (min(pieces) * remain_strings)


print(min(total, min(pieces) * strings))

### 고민
# 이럴때는 tuple를 써야할까? 
# while strings > 6: while문으로?
# 6개, 7개 남았어도 낱개를 살 순 없는건가? => catch!!

# '/'는 일반 나누기, '//' 몫을 리턴.

### 리뷰 
# 6이하 (번들 1개 or 낱개 * n)
# 6초과 (번들+낱개, 번들+1, 낱개)

### bestcode
# n, m = map(int, input().split())
# result = 0

# package, unit = [], []

# for i in range(m):
#     p, u = map(int, input().split())
#     package.append(p)
#     unit.append(u)

# p_min = min(package)
# u_min = min(unit)

# if n <= 6:
# 		# 6이하 (번들 1개 or 낱개 * n)
#     result = min(p_min, u_min * n)
# else:
# 		# 6초과 (번들+낱개, 번들+1, 낱개)
#     s = n // 6
#     r = n % 6
#     result = min(s * p_min + r * u_min, 
# 								 (s+1) * p_min, 
# 								 n * u_min)

# print(result)