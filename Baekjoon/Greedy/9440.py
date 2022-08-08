
# 숫자 더하기 (9440)
# 정답여부 : O
# 소요시간 : 1시간 17분 (15:13 ~ 16:30) 

def f(numbers):
    if len(numbers) == 0:
        numbers = [*map(int, input().split())]
    num1 = ''
    num2 = ''
    count = numbers.pop(0)
    for i in range(0, count):
        min_num = 0
        if i == 0 or i == 1:
            number_index = numbers.index(min(filter(lambda x: x > 0, numbers)))
            min_num = numbers[number_index]
            del numbers[number_index]
        else:
            number_index = numbers.index(min(numbers))
            min_num = numbers[number_index]
            del numbers[number_index]
        if i % 2 == 0:
            num1 = num1 + str(min_num)
        else:
            num2 = num2 + str(min_num)
    print(int(num1) + int(num2))
    
    new_numbers = [*map(int, input().split())]
    if len(new_numbers) == 1:
        return
    else:
        f(new_numbers)
    
nums = []
f(nums)

    
# 리뷰
# 로직을 스스로 해결했다. 함수들을 구글링했지만, 함수들을 공부하자.
# 해결과정
# https://wikidocs.net/64 (lambda, map, reduce, filter)
# 1. 변수를 input()으로 받으면서, 해당 값을 비교를 어떻게 계속 하지.. for문안에 넣을수도 없고. 함수를 써야하나?
# -> 맨 마지막에 if문으로 더할지 말지를 구분. 

# 2. 제일 작은 값부터 두 개의 배낭에 넣는다고 생각함.
# -> num1, num2에 넣는다. 
# 3. 숫자에서 string으로 변경
# -> str(), int() 참고
# 4. 최소값을 0 빼고 구해야한다. 0 빼고 구할 수 있는 조건 같은게 없나..
# -> 첫번째자리에는 0이 나올 수 없기에. 
# -> print(min(filter(lambda x: x > 0, arr)))

# 풀이2 (정리)
while True:
    numbers = list(map(int, input().split()))
    if numbers[0] == 0:
        break
    num1 = ''
    num2 = ''
    count = numbers.pop(0)
    for i in range(0, count):
        min_num = 0
        if i == 0 or i == 1:
            number_index = numbers.index(min(filter(lambda x: x > 0, numbers)))
            min_num = numbers[number_index]
            del numbers[number_index]
        else:
            number_index = numbers.index(min(numbers))
            min_num = numbers[number_index]
            del numbers[number_index]
        if i % 2 == 0:
            num1 = num1 + str(min_num)
        else:
            num2 = num2 + str(min_num)
    print(int(num1) + int(num2))
    