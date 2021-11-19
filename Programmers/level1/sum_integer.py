# 두 정수 사이의 합

def solution(a, b):
  a, b = min(a, b), max(a, b)
  return sum(i for i in range(a, b+1))

# Test
print(solution(3, 5)) # 12
print(solution(3, 3)) # 3
print(solution(5, 3)) # 12