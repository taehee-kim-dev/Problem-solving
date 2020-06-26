"""
방금 그 곡
음 종류 : C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개
1분에 한 음씩 재생
여러 개 결과 -> 재생 시간이 제일 긴 음악 -> 재생시간 같으면 먼저 입력된 음악
조건에 일치하는 음악이 없을 때 : 문자열 `(None)` 반환
"""


def str_to_note_list(notes):
    notes_in_list = []
    note_index = 0
    while note_index <= len(notes) - 1:

        one_note = notes[note_index]

        if note_index <= len(notes) - 2 and notes[note_index + 1] == '#':
            one_note += '#'
            note_index += 1

        notes_in_list.append(one_note)

        note_index += 1
    return notes_in_list


def is_heard_song(actual_played_note_list, m_note_list):

    actual_played_note_index = 0

    while actual_played_note_index <= len(actual_played_note_list) - 1:

        same_count = 1

        if actual_played_note_list[actual_played_note_index] == m_note_list[0]:

            m_note_index = 1
            tmp_actual_played_note_index = actual_played_note_index + 1

            while m_note_index <= len(m_note_list) - 1:

                if tmp_actual_played_note_index > len(actual_played_note_list) - 1:
                    break

                if actual_played_note_list[tmp_actual_played_note_index] \
                        != m_note_list[m_note_index]:
                    break

                tmp_actual_played_note_index += 1
                m_note_index += 1
                same_count += 1

        if same_count == len(m_note_list):
            return True

        actual_played_note_index += 1

    return False


def solution(m, musicinfos):
    musicinfos2 = []
    m_note_list = []

    for one_musicinfo in musicinfos:

        start_time, end_time, music_title, played_note_str = one_musicinfo.split(',')

        start_time_hour, start_time_min = map(int, start_time.split(':'))
        end_time_hour, end_time_min = map(int, end_time.split(':'))

        start_time_in_min = start_time_hour * 60 + start_time_min
        end_time_in_min = end_time_hour * 60 + end_time_min

        total_played_time = end_time_in_min - start_time_in_min + 1

        played_note_list = str_to_note_list(played_note_str)
        m_note_list = str_to_note_list(m)

        actual_played_note_list = []
        played_note_list_index = 0

        for time in range(total_played_time):

            if played_note_list_index == len(played_note_list):
                played_note_list_index = 0

            actual_played_note_list.append(played_note_list[played_note_list_index])

            played_note_list_index += 1

        musicinfos2.append([actual_played_note_list, total_played_time, music_title])

    result1 = []

    for one_musicinfo2 in musicinfos2:
        if is_heard_song(one_musicinfo2[0], m_note_list):
            result1.append(one_musicinfo2)

    if len(result1) == 0:
        return '(None)'
    elif len(result1) == 1:
        return result1[0][-1]

    result1_sorted_in_playtime = sorted(result1, key=lambda x: x[1], reverse=True)

    return result1_sorted_in_playtime[0][-1]
