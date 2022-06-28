
def solution(periods, payments, estimates):
    answer = [0] * 2
    for period, payment, estimate in zip(periods, payments, estimates):
        if period < 23:  # 다음달에도 2년이 안됨
            continue
        elif period == 23:  # 다음달부터 2년
            if sum(payment[1:]) + estimate >= 900000:  # 이번달에 90만원이 넘는 사람
                answer[0] += 1
        elif period < 59:
            if sum(payment) < 900000 and sum(payment[1:]) + estimate >= 900000:
                answer[0] += 1
            elif sum(payment) >= 900000 and sum(payment[1:]) + estimate < 900000:
                answer[1] += 1
        elif period == 59:  # 다음달부터 5년
            if sum(payment) < 900000 and sum(payment[1:]) + estimate >= 600000:
                answer[0] += 1
            elif sum(payment) >= 900000 and sum(payment[1:]) + estimate < 600000:
                answer[1] += 1
        else:
            if sum(payment) < 600000 and sum(payment[1:]) + estimate >= 600000:
                answer[0] += 1
            elif sum(payment) >= 600000 and sum(payment[1:]) + estimate < 600000:
                answer[1] += 1

    return answer


# Test
print(solution(
    [20, 23, 24],
    [
        [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],
        [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],
        [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]
     ],
    [100000, 100000, 100000]
))  # [1, 1]
print(solution(
    [24, 59, 59, 60],
    [
        [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
        [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
        [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
        [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]
     ],
    [350000, 50000, 40000, 50000]
))  # [2, 1]
