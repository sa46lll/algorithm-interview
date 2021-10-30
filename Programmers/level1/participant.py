#def solution(participant, completion):
#    for p in completion:
#        participant.remove(p)
#    return participant

def solution(participant, completion):
    n=0
    while True:
        participant.remove(completion[n])
        print(completion[n])
        n += 1
    return participant[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))