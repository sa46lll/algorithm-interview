# 하샤드 수(1)

# 숫자를 문자 배열로 변환시켜 while문으로 각 자리를 더해줌.

def solution(x):
  sum = 0
  i = 0

  while i < len(str(x)):
    sum += int(str(x)[i])
    i += 1

  if x % sum == 0:
      return True
  else: return False

# Test
print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))
