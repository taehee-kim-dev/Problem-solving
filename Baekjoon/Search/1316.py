"""
그룹 단어 체커

그룹 단어 : 단어 안에 존재하는 모든 종류의 문자는 각각 모여있어야 한다.
"""

N = int(input())

total_count_of_group_word = 0

for _ in range(N):

    input_word = input()
    char_list_of_current_word = []
    current_char = ' '
    is_group_word = True

    # 입력받은 단어의 문자를 처음부터 하나씩 검사
    for char_index in range(len(input_word)):

        # 만약 현재 검사되는 문자가 이전 문자와 다르다면
        if current_char != input_word[char_index]:
            # 이전 문자를 리스트에 저장
            char_list_of_current_word.append(current_char)
            # 이전 문자를 현재 문자로 교체
            current_char = input_word[char_index]

            # 현재 검사되고있는 문자가 이전에 나온 문자라면
            if current_char in char_list_of_current_word:
                # 이 단어는 그룹 단어가 아니다.
                is_group_word = False
                # 현재 단어에 대한 검사 종료.
                break

    if is_group_word:
        total_count_of_group_word += 1


print(total_count_of_group_word)

