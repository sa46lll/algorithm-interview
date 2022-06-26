# 내적

def solution(a, b):
    temp =  [a[i] * b[i] for i in range(len(a))]
    return sum(temp)

print(solution([1,2,3,4], [-3,-1,0,2]))