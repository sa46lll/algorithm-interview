# 스택/큐
# 기능 개발

def solution(progresses, speeds):
    answer = []
    # ceil 대신 음수로 바꿔 올림하는 벙법 # math.ceil((100-progress)//speed) 와 같음.
    day_left = [-((progress - 100) // speed) for progress, speed in zip(progresses, speeds)]

    idx = 0
    cnt = 1
    for i in range(1, len(day_left)):
        if day_left[idx] >= day_left[i]:
            cnt += 1
        else:
            answer.append(cnt)
            idx = i
            cnt = 1
    answer.append(cnt)
    return answer


# Test
print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]
print(solution([95, 95, 95, 95, 95], [1, 1, 1, 1, 1]))  # [5]
