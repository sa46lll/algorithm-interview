# 큰 수의 법칙(2) - better answer

# n개의 숫자를 입력받고 m번을 더하여 가장 큰 수를 만드는 법칙
# 특정한 인덱스가 연속하여 k개를 초과하지 않아야 한다. (k <= m)

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1))*k # 리스트 규칙
count += m % (k+1)

result = 0
result += first * count
result += second * (m-count)

print(count, result)
