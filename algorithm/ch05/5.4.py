# 재귀 함수 2 예제

# 반복 n!
def factorial_interative(n):
  result = 1
  for i in range(1, n+1):
    result *= i
  return result

# 재귀 n!
def factorial_recursive(n):
  if n <= 1:
    return 1
  return n * factorial_recursive(n-1)

# 2 sec

import time
start = time.time()
print("반복적으로 구현:", factorial_interative(5))
end = time.time()
print("WorkingTime: {} sec".format(end-start))

# 1sec

start = time.time()
print("재귀적으로 구현:", factorial_recursive(5))
end = time.time()
print("WorkingTime: {} sec".format(end-start))