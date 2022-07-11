# 완주하지 못한 선수 (해시)

def solution(participant, completion):
    d = {}
    for x in participant:
        d[x] = d.get(x, 0) + 1  # get 함수 -> x가 존재하면 해당하는 값을, 없으면 0
    for x in completion:
        d[x] -= 1
    dnf = [k for k, v in d.items() if v > 0]
    answer = dnf[0]
    return answer


# test
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))  # "leo"
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))  # "mislav"
