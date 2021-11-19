# 나머지가 1이 되는 수 찾기

def solution(n):
    i = 2
    while True:
        if n%i == 1:
            return i
        else : i += 1
    return i

# Test
print(solution(10)) #3
print(solution(12)) #11