# # 콜라츠 추측

count = 0

def solution(num):
  global count
  if num == 1:
    return count
  elif count >= 500:
    return -1

  if num % 2 == 0:
    num //= 2
    count += 1
  else:
    num = num * 3 + 1
    count += 1
  return solution(num)

print(solution(6))
print(solution(16))
print(solution(626331))

# while문

# count = 0

# def solution(num):
#   count = 0
#   while count < 500:
#     if num == 1:
#       return count
#     if num % 2 == 0:
#       num /= 2
#       count += 1
#       # print(num, count)
#     else:
#       num = num * 3 + 1
#       count += 1
#       # print(num, count)
#   if count > 500:
#     return -1

#   return count

# print(solution(6))
# print(solution(16))
# print(solution(626331))
