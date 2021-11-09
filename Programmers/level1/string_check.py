# 문자열 다루기

def solution(s):
    return True if (len(s) == 4 or len(s) == 6) and s.isdigit() else False

# Test
print(solution("a1234")) # False
print(solution("1234")) # True
