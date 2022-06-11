# 월간 코드 챌린지 시즌2
# 음양 더하기

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        answer += absolutes[i] if signs[i] else -absolutes[i]
    return answer


def solution2(absolutes, signs):
    return sum([absolute if sign else -absolute for absolute, sign in zip(absolutes, signs)])


# Test
print(solution([4, 7, 12], [True, False, True]))  # 9
print(solution([1, 2, 3], [False, False, True]))  # 0
