# 김윤현

#불린 숫자 위에 -1 
#각 열,행,대각선의 합이 -5가 되는 순간 빙고 
#사회자가 숫자 부를때 마다 빙고 체크  

bingo = [list(map(int, input().split())) for _ in range(5)]
host = [list(map(int, input().split())) for _ in range(5)]

count = 0 
bingo_count = 0 

for i in range(5):
    for j in range(5):
        tmp1 = 0 # 기로
        tmp2 = 0 # 세로
        tmp3 = 0 # 우상향
        tmp4 = 0 # 우하향
        count +=1
        for k in range(5):
            for l in range(5):
                if host[i][j] == bingo[k][l]:
                    bingo[k][l] = -100
                    tmp1 = k 
                    tmp2 = l 
        
        if sum(bingo[tmp1]) == -500:
            bingo_count +=1 
        if sum([t[tmp2] for t in bingo]) == -500:
            bingo_count +=1
        # 가로, 세로 빙고 구분 (한번에 2개 될 수 있음)
        ## 아래는 그 전 코드
        # if sum(bingo[tmp1]) == -500 or sum([t[tmp2] for t in bingo]) == -500:
        #     bingo_count +=1
        
        if tmp1 == tmp2:
            for a in range(5):
                tmp3+=bingo[a][a]
        
        if (tmp1,tmp2)==(0,4) or (tmp1,tmp2)==(1,3) or (tmp1,tmp2)==(2,2) or (tmp1,tmp2)==(3,1) or (tmp1,tmp2)==(4,0):
            for a in range(5):
                tmp4+=bingo[4-a][a]
        
        if tmp3 == -500:
            bingo_count+=1
        
        if tmp4 ==-500:
            bingo_count+=1 
        
        ## 아래 구문 추가 
        ## 만약 j가 2인데, 아래 구문이 없으면
        ## j = 3, j = 4 경우도 해서 count가 2 늘어남. 
        if bingo_count >= 3:
            break
            
    if bingo_count >= 3:
        print(count)
        break

                    