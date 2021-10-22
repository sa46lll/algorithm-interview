# 3진법 뒤집기

def solution(n):
    result = ''
    i = 3
    tmp = 0
    a = 0
    while a > 0:
        a, b = divmod(n, i.sqrt(tmp))
    max = i-1
    print(max)

    # for i in range(1, max, -1):
    #   result += str(n//i)
    #   n %= i
    # print(result)
    return
# return result[::-1]   

print(solution(45))
# print(solution(125)