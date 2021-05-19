# 이진수 (2406)
# 정답여부 : O 
# 소요시간 : 11분 (10:29 ~ 10:40)


n = int(input())
for i in range(n):
    num = int(input())
    one_index = 0

    while(num // 2 != 0):
        if num % 2 == 1:
            print(one_index, end=' ')
        num = num // 2
        one_index += 1
    print(one_index, end=' ')

# 리뷰
# 1을 가진 index를 one_index 라고 변수명을 지었다.
#
# # 헤맨점
# 문제에서 테스트케이스 개수가 있다는 말이 이해가 되지 않아서
# 약간 헤맸다.
# 설명 : 테스트케이스 개수가 주어지고, 그 만큼의 테스트 케이스가 주어지는 것.
# ex.
# 2  # testcase가 2이면, 13, 16 총 input가 2개가 존재하는 것
# 13
# 15


