# 완주하지 못한 선수

# sol1)
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()


# sol2)
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# Test
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))