# 문제
# N에서 1을 뺀다. 혹은 N을 K로 나눈다. 
# 둘 중 하나를 선택하여 N이 1이 될 때까지 한다.
# N이 1이 되는 최소 횟수를 구하여라.
# 입력조건
# 첫째 줄에 N과 K가 공백으로 구분되며 각각 자연수로 주어진다. 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.
# 출력조건
# 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번 과정을 수행해야하는 횟수의 최솟값을 구한다.

# 입력예시
# 25 5
# 출력예시
# 2

# 해설 : 나눌 수 있으면 무조건 나누는게 횟수가 적다.

n, k = map(int, input('N과 K를 입력해주세요 : ').split())
result = 0

while True:
    target = (n//k) * k
    result += (n-target)
    n = target
    if n<k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)

