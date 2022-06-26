# 정수 제곱근 판별
from math import sqrt

def solution(n):
    if sqrt(n) % 1 == 0:
        return int(sqrt(n)+1) ** 2
    return -1

# Test
print(solution(121)) # 144
print(solution(3)) # -1