# 숫자 문자열과 영단어

def solution(s):
    strings = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for string in strings:
      if string in s:
        s = s.replace(string, str(strings.index(string)))
      
    return s

# Test
print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("1zerotwozero3"))