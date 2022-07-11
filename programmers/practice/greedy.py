# 체육복 (그리디)
# n이 크지 않을 경우

def solution(n, lost, reserve):
    u = [1] * (n + 2)
    for i in lost:
        u[i] -= 1
    for i in reserve:
        u[i] += 1
    for i in range(1, n + 1):
        if u[i - 1] == 0 and u[i] == 2:
            u[i-1:i+1] = [1, 1]
        elif u[i] == 2 and u[i + 1] == 0:
            u[i:i+2] = [1, 1]
    answer = len([x for x in u[1:-1] if x > 0])
    return answer


# test
print(solution(5, [2, 4], [1, 3, 5]))  # 5

# 시간 복잡도 O(n) = n
