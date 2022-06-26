# 시저 암호

def solution(s, n):
    a = ''
    for i in range(len(s)):
      if ord(s[i])+n >= 123:
        n -= 26
        a += chr(ord(s[i])+n)
      elif s[i] == ' ':
        a += ' '
      else: a += chr(ord(s[i])+n)
    return a

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))

