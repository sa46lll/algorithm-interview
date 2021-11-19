# def solution(s):
#   result = ''
#   for i in range(len(s)):
#     if i % 2 ==0:
#       result += s[i].upper()
#     else: result += s[i]
#   return result

# print(solution('try hello world'))

def solution(s):
  result = ''
  s = list(s.split())
  n = 0
  while True:
    for i in range(len(s[n])):
      result += s[i].upper() if i % 2 == 0 else s[i].lower()
    result += " "
    n += 1
  return result

print(solution("try hello world"))