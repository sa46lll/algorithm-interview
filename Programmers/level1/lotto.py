# 2021 Dev-Matching
# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    win_min = 0
    for lotto in lottos:
        if lotto in win_nums:
            win_min += 1
    win_max = win_min + lottos.count(0)

    rank_min = 7 - win_min
    rank_max = 7 - win_max
    answer = [rank_max, rank_min if rank_min<7 else 6]
    return answer


# Test
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))  # [3,5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))  # [1,6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))  # [1,1]

