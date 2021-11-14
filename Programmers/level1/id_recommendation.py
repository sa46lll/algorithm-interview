# 신규 아이디 추천

import re
def solution(new_id):
    # 여러문자 치환 (참고 - https://www.delftstack.com/ko/howto/python/python-replace-multiple-characters/)
    answer = re.sub('[^0-9a-z_.\-]+','',new_id.lower())
    answer = re.sub('\.\.+','.',answer)

    # 양끝 문자열 제거
    answer = answer.strip('.')

    # 빈 문자열 예외
    if not answer: answer='a'

    # 15개 문자 추출, 마침표 제거
    answer = answer[:15].rstrip('.')

    if len(answer)<=2:
      answer += answer[-1]*(3-len(answer))
    
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("ab"))