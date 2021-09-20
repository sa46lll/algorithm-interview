n, m = map(int, input().split())
d = [[0] * m  for _ in range(n)] # 방문 지도 초기화
x, y, direction = map(int, input().split())
d[x][y] = 1 # 시작하는 위치 방문표시

array = []
for i in range(n):
  array.append(list(map(int, input().split())))
print(array)

dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]

count = 0