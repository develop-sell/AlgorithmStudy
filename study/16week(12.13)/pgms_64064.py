# 프로그래머스: 불량 사용자(64064)
# 조합, 순열 문제인데 헷갈렸다.

'''
경우의수 문제.
visited로 해서.

한 뭉텅이씩 계산되고 다시 곱하고. 
만약 이미 visited된 숫자면 곱할때는 곱하되 -1 를 해준다. 이게 핵심 - 5:55 이해 완료
'''

banned_id = ["fr*d*", "abc1**"]
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]

# banned_id = ["*rodo", "*rodo", "******"]
# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]

# banned_id = ["fr*d*", "*rodo", "******", "******"]
# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]



## 두번째 코드
'''
제재 아이디 목록들을 구했을 때 아이디들이 나열된 순서와 
관계없이 아이디 목록의 내용이 동일하다면 같은 것으로 처리하여 하나로 세면 됩니다.

위 조건에 의해. 그리고 데이터 크기가 많지 않기에.
배열 자체를 key값으로 저장하든 해서 있는지 없는지확인해야할듯.

123 -> 이런 키값으로 dict에 저장할 것.
이미 있는지 없는지 set으로 확인 가능하니까. 
sort해서 값 비교. 
'''

from itertools import permutations, combinations

# 같은지 체크해주는 것.
def check(u_ids,b_ids):
    for i in range(len(u_ids)):
        # 길이부터 다르면 제외
        if len(u_ids[i]) != len(b_ids[i]):
            return False
        for j in range(len(u_ids[i])):
            # 같거나, *면 패스
            if b_ids[i][j] == "*" or b_ids[i][j] == u_ids[i][j]:
                continue
            else:
                return False
    return True

'''
user_id를 banned_id len만큼 조합으로 만들고.
그 안에서 순열로 만들어서 check를 확인.
만약 check가 확인되면 break후 result +1 
'''

ans = 0
for t in combinations(user_id, len(banned_id)):
    for tt in permutations(t, len(banned_id)):
        if check(tt, banned_id):
            ans += 1
            break


print(ans)


## 처음 코드  -> 문제 잘못 이해
'''
visited = [0] * len(user_id)


ans = 1

# 같은지 체크해주는 것.
def check(u_id,b_id):
    for i in range(len(u_id)):
        if b_id[i] == "*" or u_id[i] == b_id[i]:
            continue
        else:
            return False
    return True


for cur in banned_id:
    cnt = 0
    minus = 0
    for i in range(len(user_id)):
        if len(user_id[i]) == len(cur) and check(user_id[i], cur):
            if visited[i] == -1:
                minus += 1
            cnt += 1
            visited[i] = -1
    
    ans *= cnt
    ans -= minus

print(ans)
'''