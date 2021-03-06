# 인접 행렬 방식(Adjacency Matrix) 예제

# 2차원 배열로 각 노드가 연결된 형태를 기록하는 방식

INF = 99999999 
# 무한의 비용 선언
# 실제 코드에서 논리적으로 정답이 될수 없는 큰값 중에서 999999999, 987654321 등의 값으로 초기화하는 경우 많음.

graph = [
  [0, 7, 5],
  [7, 0, INF],
  [5, INF, 0],
]

print(graph)

# DFS(Depth-First Search)

# 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘