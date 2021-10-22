def solution(a, b):
    month_days = [31, 30, 31, 29, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['금', '토', '일', '월', '화', '수', '목']
    days = 0
    if a == 1:
      days = b-1
    else: 
      for i in range(a-1):
        # print(month_days[i])
        days += month_days[i]
      days += (b-a) -1
      # print(days%7)
    return day[days%7]

print(solution(5, 24))

# '금', '토', '일', '월', '화', '수', '목'