# 인접 리스트 방식(Adjacency List) 예제

# 인접 행렬과 같이 2차원 리스트를 이용하면 됨.

# C++나 자바같은 언어에서는 연결 리스트 기능을 위한 표준 라이브러리 제공.

graph = [[] for _ in range(3)]

# 노트 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노트 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))

# 노트 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5))


print(graph)