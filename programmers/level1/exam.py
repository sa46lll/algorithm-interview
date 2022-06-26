# 모의고사
def solution(answers):
    std1 = [1, 2, 3, 4, 5]
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0] * 3
    max_score_std = []

    for idx, answer in enumerate(answers):
        print(idx, answer)
        if answer == std1[idx % len(std1)]:
          score[0] += 1
        if answer == std2[idx % len(std2)]:
          score[1] += 1
        if answer == std3[idx % len(std3)]:
          score[2] += 1
    
    for idx, s in enumerate(score):
        if s == max(score):
            max_score_std.append(idx + 1)
    
    return max_score_std
    # return



# print(solution([1,2,3,4,5]))
print(solution([1, 3, 2, 4, 2]))