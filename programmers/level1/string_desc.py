# 문자열 내림차순으로 배치하기

def solution(s):
  result = sorted(s, reverse=True)
  return ''.join(result)

# Test
print(solution("Zbcdefg"))