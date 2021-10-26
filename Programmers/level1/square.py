# 멀쩡한 사각형

# sol1) 런타임 에러 (x좌표를 이용해 계산))

# import math

# w, h = min([w, h]), max([w, h])
# def solution(w,h):
#     list = [w/h * i for i in range(h+1)]
#     minus_square = 0
#     for i in range(h):
#         minus_square += math.ceil(list[i+1]) - math.floor(list[i])
#     return w * h - minus_square


# sol2) 최소공배수를 이용한 계산

import math

def solution(w,h):
    return w * h - (w + h - math.gcd(w, h))

# Test
print(solution(8, 12))
print(solution(4, 7))