# 소수 찾기

from itertools import permutations

def solution(numbers):
    items = list(str(numbers))
    combinations = []
    for i in range(1, len(items)+1):
        combinations += list(permutations(items, i))
        # print(combinations)
    combinations = [int("".join(c)) for c in combinations]

    result = True
    prime = 0
    for combination in combinations:
        # print(combination)
        for i in range(2, combination):
            if combination < 2 or combination % i == 0:
                print(combination, "False")
                # array.append(combination)
                break
        if result:
          # print(combination, "True")
          prime += 1
        
    return prime

print(solution(17))
# print(solution(011))
