# 음료수 얼려 먹기

# 얼음 묶음이 몇개 생성되는지.. 
N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int,input())))

def dfs(x, y):
    # 범위 넘어가면 False
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    # 상, 하, 좌, 우 순으로 스택에 push. 방문한 경우 False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y) # 상
        dfs(x+1, y) # 하
        dfs(x, y-1) # 좌
        dfs(x, y+1) # 우
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
       if dfs(i, j) == True:
            result += 1

print(result)