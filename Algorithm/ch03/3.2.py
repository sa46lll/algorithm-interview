# 큰 수의 법칙

# n개의 숫자를 입력받고 m번을 더하여 가장 큰 수를 만드는 법칙
# 특정한 인덱스가 연속하여 k개를 초과하지 않아야 한다. (k <= m)

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 원본이 정렬됨.
first = data[n-1] # 가장 큰수
second = data[n-2] # 두번째 큰수

result = 0

while True: # first, second 반복
  for i in range(k): # first 를 합산
    if m == 0:
      break
    result += first
    m -= 1
  if m == 0: # second 를 합산
    break
  result += second
  m -= 1

print(result)

