# 2020 카카오 인턴십
# 키패드 누르기

def keypad_distance(currentN, nextN):  # 키패드 사이의 거리
    keypad = {1: [0, 0], 2: [1, 0], 3: [2, 0],
              4: [0, 1], 5: [1, 1], 6: [2, 1],
              7: [0, 2], 8: [1, 2], 9: [2, 2],
              "*": [0, 3], 0: [1, 3], "#": [2, 3]}

    cur_x, cur_y = keypad[currentN]
    next_x, next_y = keypad[nextN]
    return abs(cur_x - next_x) + abs(cur_y - next_y)


def solution(numbers, hand):
    result = ''
    current_left, current_right = "*", "#"
    hand = 'L' if hand == 'left' else 'R'

    for number in numbers:
        if number in [1, 4, 7]:
            result += 'L'
            current_left = number
        elif number in [3, 6, 9]:
            result += 'R'
            current_right = number
        else:
            # 2, 5, 8, 0
            left_distance = keypad_distance(current_left, number)
            right_distance = keypad_distance(current_right, number)
            if left_distance < right_distance:
                result += 'L'
                current_left = number
            elif left_distance > right_distance:
                result += 'R'
                current_right = number
            else:
                result += hand
                if hand == 'L':
                    current_left = number
                else:
                    current_right = number

    return result


# Test
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))  # "LRLLLRLLRRL"
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))  # "LRLLRRLLLRR"
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))  # "LLRLLRLLRL"
