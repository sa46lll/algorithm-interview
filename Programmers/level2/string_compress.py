# 2020 kakao blind recruitment
# 문자열 압축

def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]  # 반복되는 문자열
        count = 1  # 반복되는 문자열에 대한 횟수

        for j in range(step, len(s), step):
            # prev 문자열과 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:  # 문자열 슬라이싱 이용
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]  # 다시 상태 초기화
                count = 1

        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))

    return answer


# Test
print(solution("aabbaccc"))  # 2a2ba3c -> 7
print(solution("ababcdcdababcdcd"))  # 2ababcdcd -> 9

