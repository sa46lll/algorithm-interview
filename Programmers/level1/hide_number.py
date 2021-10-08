# 핸드폰 번호 가리기

# replace 함수를 이용하여 문자열 [:-4] -> "*" 로 바꿔줌.

def solution(phone_number):
  return phone_number.replace(phone_number[:-4], "*" * len(phone_number[:-4]), 1)

# Test
print(solution("01012341234"))
print(solution("01033334444"))
print(solution("027778888"))