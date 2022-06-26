# 체육복

def solution(n, lost, reserve):

  set_lost = set(lost) - set(reserve) # 여벌옷 없는 사람
  set_reserve = set(reserve) - set(lost) # 도난당한 후에도 여벌옷 있는 사람
  print(set_lost)
  print(set_reserve)


  for r in list(set_lost):
    if r-1 in set_reserve:
      set_lost.remove(r)
      set_reserve.remove(r-1)
    elif r+1 in set_reserve:
      set_lost.remove(r)
      set_reserve.remove(r+1)
    print("여벌옷 못빌리는사람",set_lost)
    print("여벌옷 남는 사람",set_reserve)
  return n - len(set_lost)

print(solution(5, [2, 4], [1, 3, 5]))