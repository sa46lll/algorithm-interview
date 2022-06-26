# 조이스틱

def push_count(name):
    count = 0
    for alph in name:
        count += min(ord("Z")-ord(alph) + 1, ord(alph)-ord("A"))
    return count

def solution(name):
    min_move = len(name) - 1
    for i, char in enumerate(name):
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        min_move = min(min_move, i + i + len(name) - next)
    answer = push_count(name)
    answer += min_move
    return answer

# Test
print(solution("JEROEN")) #56
print(solution("JAN"))    #23
print(solution("JAZ"))    #11