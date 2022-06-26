# 숫자 카드 게임

# 여러 개의 숫자 카드 중에 가장 높은 숫자가 쓰인 카드 한장을 뽑는 게임
# n * m 형태로 놓여있음

n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)
  result = max(result, min_value)

print(result)