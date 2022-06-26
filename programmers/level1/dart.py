# 다트 게임

def solution(dartResult):
    stack = []
    dartResult = dartResult.replace("10", "A")
    bonus = {'S': 1, 'D': 2, 'T': 3}
    
    # 회차별로 계산
    for dart in dartResult:
        if dart.isdigit() or dart=='A':
            stack.append(10 if dart == 'A' else int(dart))
        elif dart in ('S', 'D', 'T'):
            num = stack.pop()
            stack.append(num ** bonus[dart])
        elif dart == '#':
            stack[-1] *= -1
        elif dart == '*':
            num = stack.pop()
            if len(stack):
                stack[-1] *= 2
            stack.append(2 * num)
    return sum(stack)

# Test
print(solution("1S2D*3T")) #37
print(solution("1D2S#10S")) #9