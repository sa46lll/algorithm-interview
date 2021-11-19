# 1이 될 때까지(2)

# 어떠한 수 n이 1이 될 때까지 다음 두 과정을 반복적으로 수행하려 한다.

n, k = map(int, input().split())

count = 0

while True:
  remainder = n % k # remainder k로 나눈 나머지
  n -= remainder # 나머지를 빼주면서 n은 나눠떨어지는 수가 됨.
  count += remainder
  if n < k:
    break
  n //= k 
  count += 1

# 남은 수 1씩 빼주기
count += (n-1)
print(count)