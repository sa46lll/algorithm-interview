
def solution(p):
    answer = [0] * len(p)
    for idx, value in enumerate(p):
        if value != min(p[idx:]):
            min_val = min(p[idx:])
            answer[idx] += 1
            answer[p.index(min_val)] += 1
            # 자리 바꿈
            temp = p[p.index(min_val)]
            p[p.index(min_val)] = p[idx]
            p[idx] = temp
            idx += 1
        else:
            idx += 1

    return answer


# Test
print(solution([2, 5, 3, 1, 4]))  # [1, 1, 0, 3, 1]
print(solution([2, 3, 4, 5, 6, 1]))  # [1, 1, 1, 1, 1, 5]
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # [0, 0, 0, 0, 0, 0, 0, 0, 0]
