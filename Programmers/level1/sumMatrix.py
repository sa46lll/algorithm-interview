# 행렬의 덧셈

# arr3라는 새로운 변수를 만들어 arr1, arr2의 합을 입력함.

def solution(arr1, arr2):
  arr3 = [[0] * len(arr1[0]) for _ in range(len(arr1))]
  for i in range(len(arr1)):
    for j in range(len(arr1[0])):
      arr3[i][j] = arr1[i][j] + arr2[i][j]
  return arr3

# Test
print(solution([[1,2,3],[3,4,5]], [[3,4,5],[7,8,9]]))
print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
print(solution([[1],[2]], [[3],[4]]))

