# 큐 예제

# 선입선출: 나중에 온 사람일수록 나중에 들어감(공정한 자료구조라고도 함)
from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5) # 5
queue.append(2) # 5 2
queue.append(3) # 5 2 3
queue.append(7) # 5 2 3 7
queue.popleft() # 2 3 7
queue.append(1) # 2 3 7 1
queue.append(4) # 2 3 7 1 4
queue.popleft() # 3 7 1 4

print(queue)
queue.reverse()
print(queue)

