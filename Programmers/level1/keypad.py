# 키패드 누르기 - 미완

def solution(numbers, hand):
    result = ''
    for number in numbers:
        if number in [1, 4, 7]:
            result += 'L'
            last_number = number
        elif number in [3, 6, 9]:
            result += 'R'
            last_number = number
        else:
            # return
            if last_number: # last_number가 존재한다면..
              

    return result

# Test
# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))

print(solution([1, 4, 7, 3, 6, 9], "right"))
