# 문제
# 주어진 수들을 이용해 M번 더하여 가장 큰 수를 만들어라. 특정 인덱스의 수는 K번 이상 사용할 수 없다.
# N개의 리스트를 제공한다.
# 입력조건
# 1. 첫째 줄에 N(2~1,000), M(1~10,000), K(1~10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 2. 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1이상 10,000 이하의 수로 주어진다.
# 3. 입력으로 주어지는 K는 항상 M보다 작거나 같다.
# 출력조건
# 큰 수의 법칙에 따라 더해진 답을 출력한다.

# 입력예시
# 5 8 3
# 2 4 5 4 6

# 해설
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input('n,m,k를 입력해주세요 : ').split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input('N 데이터를 입력해주세요 : ').split()))

data.sort() #입력받은 수들 정렬하기
first = data[n-1] # 가장 큰수
second = data[n-2] # 두 번째로 큰수

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m==0:
        break
    result += second
    m -= 1
    
print(result)
        
