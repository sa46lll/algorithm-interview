# 나누어 떨어지는 수

def solution(arr, divisor):
result = sorted([num for num in arr if num % divisor == 0])
return [-1] if not result else result