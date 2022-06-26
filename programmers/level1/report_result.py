# 2022 kakao blind recruitment
# 신고 결과 받기

from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}
    
    for r in set(report):
      reports[r.split()[1]] += 1
    
    for r in set(report):
      if reports[r.split()[1]] >= k:
        answer[id_list.index(r.split()[0])] += 1

    return answer

# Test
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))  # [2,1,1,0]
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))  # [0,0]
