def solution(phone_number):
  return phone_number.replace(phone_number[:-4], "*" * len(phone_number[:-4]), 1)

print(solution("01012341234"))
print(solution("01033334444"))
print(solution("027778888"))