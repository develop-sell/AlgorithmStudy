# 피보나치수 5 (10870)
# 정답여부 : O 
# 소요시간 : 17분 (10:03 ~ 10:20)

index = int(input())
if index == 0:
    print(0)
elif index == 1:
    print(1)
else:
    index_minus_2 = 0
    index_minus_1 = 1
    for i in range(2, index):
        temp = index_minus_1
        index_minus_1 = index_minus_1 + index_minus_2
        index_minus_2 = temp
    print(index_minus_1 + index_minus_2)

# 리뷰 
# 처음에는 n-2, n-1의 숫자의 합만 갖고 있으려고 생각해서
# 결국 n-1의 값만 가지도록 짰다.
# 또한 temp라는 임시 변수를 사용하지 않으면,
# 기존의 n-1 혹은 n-2가 변경된 상태로 새로운 n-1 값을 구하기 때문에 문제가 발생한다.
#
# 그리고 역시 직접 손으로 쓰면서 해보는 것이 빨리 풀 수 있는 방법이다.
#
# # 헤맨점
# temp 변수를 두지 못한 점. 그래서 좀 오래 걸렸다.