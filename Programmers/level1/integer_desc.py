# 정수 내림차순으로 배치하기

def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))

# Test
print(solution(118372))