# 2019 kakao blind recruitment =
# 오픈채팅방

def solution(record):
    answer = []
    uid_dict = {}
    for sentence in record:
        sentence_split = sentence.split()
        # Enter, Change -> {'id': 'name'} 회원 저장
        if len(sentence_split) > 2:  # sentence.startswith(''), sentence_split[0] in ['Enter', 'Change'] 를 써도 좋다
            uid_dict[sentence_split[1]] = sentence_split[2]

    for sentence in record:
        sentence_split = sentence.split()
        if sentence_split[0] == 'Enter':
            answer.append(f"{uid_dict[sentence_split[1]]}님이 들어왔습니다.")
        elif sentence_split[0] == 'Leave':
            answer.append(f"{uid_dict[sentence_split[1]]}님이 나갔습니다.")

    return answer


# Test
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
                "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
