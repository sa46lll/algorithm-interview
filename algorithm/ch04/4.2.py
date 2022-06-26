import time
start = time.time()

# 왕실의 나이트

# 나이트가 8*8 체스판에서 이동할 수 있는 경우의 수
data = input()

col = int(ord(data[0]))-int(ord('a')) + 1 # 문자를 숫자로 변환
row = int(data[1])
count = 0

moves = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

for move in moves:

  next_col = col + move[0]
  next_row = row + move[1]

  # sol1)
  if next_col <= 8 and next_col >= 1 and next_row <= 8 and next_row >= 1:
    count += 1

  # sol2)
  # if next_col > 8 or next_col < 1 or next_row > 8 or next_row < 1:
  #   continue
  # count += 1

print(count)

# 2 sec

end = time.time()
print("WorkingTime: {} sec".format(end-start))