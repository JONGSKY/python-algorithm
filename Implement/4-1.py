# 문제
# N*N 크기의 정사각형 공간에서 우리는 (1,1) 위치에 있다.
# - L : 위쪽으로 한 칸 이동
# - R : 오른쪽으로 한 칸 이동
# - U : 위로 한 칸 이동
# - D : 아래로 한 칸 이동
# 이동 후에 있는 위치를 구해라

# 입력조건
# 1. 첫째 줄에 공간의 크기를 나타내느 N이 주어진다. (1<=N<=10)
# 2. 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1<=이동횟수<=100)

# 출력조건
# 1. 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X,Y)를 공백으로 구분하여 출력한다.

# 입력예시
# 5
# R R R U D D

#출력예시
# 3 4

# 해설

# N을 입력받기
n = int(input())
x, y = 1,1
plans = input().split()

#L,R,U,D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

#이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx >n or ny < n:
        continue
    # 이동 수행
    x , y = nx, ny

print(x, y)