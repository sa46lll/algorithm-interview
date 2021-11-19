import time
start = time.time()

# 상하좌우

# L:왼쪽, R: 오른쪽, U: 위 D: 아래

n = int(input())
x, y = 1, 1

moves = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for move in moves:
  if move in move_types:
    i = move_types.index(move)
    nx = x + dx[i]
    ny = y + dy[i]
  if nx > n or ny > n or nx < 1 or ny < 1:
    continue
  x = nx
  y = ny

print(x, y)

# 4 sec

end = time.time()
print("WorkingTime: {} sec".format(end-start))
