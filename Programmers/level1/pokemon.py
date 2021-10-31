# 폰켓몬

import itertools

def solution(nums):
    return len(set(nums)) if len(nums) / 2 > len(set(nums)) else len(nums) / 2

# Test
print(solution([3,1,2,3]))

# A if 조건 else B