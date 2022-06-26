# 선택 정렬 소스코드

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]: # index_j가 더 작을 때 min_index 와 교환
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)
