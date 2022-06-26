# 카카오 개발자 겨울 인턴십
# 크레인 인형뽑기

def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        for b in range(len(board)):
            if board[b][move-1] != 0:
                basket.append(board[b][move-1])  # basket 에 채워 주고
                board[b][move - 1] = 0  # 보드는 0으로 바꿔줌
                break

    i = 1
    while i < len(basket):
        if basket[i-1] == basket[i]:
            answer += 2
            basket.pop(i - 1)
            basket.pop(i - 1)
            i = 1
        else:
            i += 1
    return answer


# Test
print(solution([[0, 0, 0, 0, 0],
                [0, 0, 1, 0, 3],
                [0, 2, 5, 0, 1],
                [4, 2, 4, 4, 2],
                [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))  # 4
