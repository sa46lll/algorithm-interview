# 체육복 (그리디 2)
# n이 매우 크고, lost 나 reserve 의 길이가 짧은 경우

def solution(n, lost, reserve):
    s = set(lost) & set(reserve)
    l = set(lost) - s  # 운동복이 없는 학생
    r = set(reserve) - s  # 운동복 여벌이 있는 학생

    for x in sorted(r):
        if x - 1 in l:
            l.remove(x-1)
        elif x + 1 in l:
            l.remove(x+1)
    answer = n - len(l)
    return answer


# test
print(solution(5, [2, 4], [1, 3, 5]))  # 5
print(solution(5, [2, 4], [3]))  # 4

# 시간 복잡도 O(n) = nlogn
