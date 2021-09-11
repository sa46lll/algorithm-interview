# 1이 될 때까지

# 어떠한 수 n이 1이 될 때까지 다음 두 과정을 반복적으로 수행하려 한다.

n, k = map(int, input().split())

count = 0

while n >= k:
  # 나눠 떨어지지 않을 때 n-1
  while n%k != 0:
    n -= 1
    count += 1
  n //= k
  count += 1

while n != 1:
  n -= 1
  count += 1

print(count)