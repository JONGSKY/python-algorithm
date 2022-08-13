# 문제
# 정수 N이 입력되면 00시00분000초부터 N시59분59초까즹 모든 시각 중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.

# 입력조건
# 1. 첫째 줄에 정수 N이 입력된다. (0<=N<=23)

# 출력조건
# 1. 00시 00분 00초로부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.

# 입력예시
# 5

#출력예시
# 11475

# 해설
# 모든 경우의 수는 86,400가지 밖에 존재하지 않음. 따라서 그냥 다 확인해도 문제 없음
# H를 입력받기
h = int(input('숫자 N을 입력해주세요 : '))

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있는지 확인
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)