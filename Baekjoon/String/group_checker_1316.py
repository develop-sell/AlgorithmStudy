# 그룹 단어 체커 (1316)
# 8:18~8:25
n = int(input())
ans = n
for i in range(n):
    word = input()
    cur = word[0]
    chars = [word[0]]
    for c in word:
        if cur == c:
            continue
        if c in chars:
            ans += -1
            break
        else:
            chars.append(c)
            cur = c

print(ans)