# 2021 Dev-Matching
# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    cnt = 0
    cnt_zero = lottos.count(0)
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1

    answer = [7-cnt-cnt_zero if cnt+cnt_zero > 1 else 6, 7-cnt if cnt > 1 else 6]
    return answer


# Test
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))  # [3,5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))  # [1,6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))  # [1,1]
print(solution([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]))  # [6,6]

