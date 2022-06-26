# 그리디

# N원을 거슬러줘야 할 때, 동전의 최소 개수

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += n // coin
  n %= coin

print(count)