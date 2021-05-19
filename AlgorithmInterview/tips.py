#리스트 컴프리헨션 : 1 ~ 7까지 숫자 중, 짝수들을 곱하기 4한, 값들을 모아둔 리스트
calculated_list = [n * 4 for n in range(1,8) if n % 2 == 0]
print(calculated_list)

hel: int = 1 # type 지정 