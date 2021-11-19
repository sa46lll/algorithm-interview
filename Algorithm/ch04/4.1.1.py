import time
start = time.time()

# 시각

# 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력

n = int(input())

count = 0
for hour in range(n + 1):
  for min in range(60): # min
    for sec in range(60): # sec
      if '3' in str(hour)+str(min)+str(sec):
        count += 1
    
print(count)

# 1.5 sec

end = time.time()
print("WorkingTime: {} sec".format(end-start))
