# 카펫

def solution(brown, yellow):
    answer = []
    list = combinations(brown+yellow) # {(24, 2), (12, 4), (16, 3), (8, 6)}
    for i in list:
        width, height = i
        if (width-2)*(height-2) == yellow:
            # print("True")
            return [width, height]

def combinations(cnt):
    lst = []
    for i in range(2, cnt//2):
        if cnt % i == 0:
            a, b = max(cnt//i, i), min(cnt//i, i)
            lst.append([a, b])
            lst = list(map(tuple,lst))
    return set(lst)


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))