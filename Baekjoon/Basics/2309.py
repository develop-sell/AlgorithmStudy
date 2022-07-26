# 일곱난쟁이 (2309)
# 정답여부 : X
# 소요시간 : 10분 (16:39 ~ 16:49)

people = []
for i in range(9):
    people.append(int(input()))
people.sort()

total = sum(people)
for i in range(9):
    for j in range(i+1, 9):
        if total - people[i] - people[j] == 100:
            num1, num2 = people[i], people[j]
            people.remove(num1)
            people.remove(num2)

            for k in range(len(people)):
                print(people[k])
            break
    if len(people) < 9:
        break
            


# 리뷰
# 16줄에서 index bound error 뜨길래 뭐지 싶었는데, remove를 했기에 index 값이 8이었으면 error 뜰 수 밖에 없었다. 
# 21줄 remove 후 break를 list의 len로 비교해서 빠져나오는 스킬이 유용해보인다. 
# 헤맨점

# 풀이 2

