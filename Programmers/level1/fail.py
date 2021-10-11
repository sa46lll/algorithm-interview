def solution(N, stages):
    fails = []
    for stage in range(1, N+1):
        a = stages.count(stage)
        b = 0
        for i in range(len(stages)):
            if stages[i] >= stage:
                b += 1
        fail = a/b
        fails.append(fail)

    rank = []
    for i in range(N):
        print(sorted(fails)[i])
        rank.append(fails.index(sorted(fails, reverse=True)[i]) + 1)
    return rank

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

