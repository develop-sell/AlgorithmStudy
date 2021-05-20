# 최소, 최대 (10818)
# 정답여부 : O
# 소요시간 : 12분 (09:58 ~ 10:10)

count = int(input())
numbers = list(map(int, input().split()))
print(min(numbers), max(numbers), sep=" ")


# 리뷰
# string의 list의 원소를 전부 int형으로 바꾸는 방식
# 이번 기회에 꼭 외우도록 하자

# 헤맨점
# 1. 띄어쓰기로 input 받아서 list 만들기
# - input().split()
# 2. 받은 list를 int형태로 mapping해서 다시 리스트 만들기
# - list(map(int, input().split()))



