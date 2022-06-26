# 가장 큰 수

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x : x*3, reverse=True)
    return str(int(''.join(numbers)))

# Test
print(solution([6, 10, 2])) # 6210
print(solution([3, 30, 34, 5, 9])) # 9534330