# k번째로 큰 수

def solution(array, commands):
    result = []
    for command in commands:
        i, j, k = command
        result.append(list(sorted(array[i-1:j]))[k-1])
    return result

# Test
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))