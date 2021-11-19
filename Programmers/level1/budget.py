def solution(d, budget):
    d.sort()
    sum, idx = 0, 0

    # while sum <= budget:
    #     if sum == budget:
    #         return idx
    #     sum += d[idx]
    #     idx += 1
    # return idx - 1

    for d_ in d:
        sum += d_
        idx += 1
        if sum > budget:
          return idx - 1
        elif sum == budget:
          return idx
    return idx
# Test
print(solution([1,3,2,5,4], 9))
print(solution([2, 2 ,3 ,3], 10))