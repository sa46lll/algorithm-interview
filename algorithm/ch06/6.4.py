# 퀵 정령 소스코드

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quich_sort(array, start, end):
  if start >= end : # 원소가 1개인 경우 종료
    return
  pivot = start
  left = start + 1
  right = end
  while left <= right:
