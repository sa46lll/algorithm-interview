# 약수의 합

def solution(n):
    return sum([i for i in range(1, n+1) if n%i == 0])

# Test
print(solution(12)) # 28
print(solution(5)) # 6