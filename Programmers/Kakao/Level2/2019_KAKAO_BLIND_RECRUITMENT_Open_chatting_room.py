"""
2019 KAKAO BLIND RECRUITMENT
오픈채팅방
"""


def solution(record):
    answer = []

    all_user_id_and_nickname = {}
    all_user_id_and_message_in_hangul_in_chatting_room = []

    for record_line in record:

        split_record_line = record_line.split()
        message = split_record_line[0]
        user_id = split_record_line[1]
        nickname = ''

        if len(split_record_line) == 3:
            nickname = split_record_line[2]

        if message == 'Enter' or message == 'Change':
            all_user_id_and_nickname[user_id] = nickname

        if message != 'Change':
            message_in_hangul = ''
            if message == 'Enter':
                message_in_hangul = '들어왔습니다.'
            else:
                message_in_hangul = '나갔습니다.'
            all_user_id_and_message_in_hangul_in_chatting_room.append([user_id, message_in_hangul])

    for user_id_and_message_in_hangul in all_user_id_and_message_in_hangul_in_chatting_room:
        answer.append(all_user_id_and_nickname[user_id_and_message_in_hangul[0]] + '님이 ' + user_id_and_message_in_hangul[1])

    return answer
