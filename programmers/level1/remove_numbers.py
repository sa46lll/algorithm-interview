# 없는 숫자 더하기

def solution(numbers):
    list = [i for i in range(10)]
    sub_list = [x for x in list if x not in numbers]
    return sum(sub_list)

# Test
print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))
