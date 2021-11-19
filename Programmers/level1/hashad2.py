# 하샤드 수(2)

# map을 이용하여 배열을 정수로 모두 변환하고, 총합을 한번에 계산함.

def solution(x):

  list_ = list(str(x))
  list_ = list(map(int, list_))
  sum_ = sum(list_)

  if x % sum_ == 0:
      return True
  else: return False

# Test
print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))