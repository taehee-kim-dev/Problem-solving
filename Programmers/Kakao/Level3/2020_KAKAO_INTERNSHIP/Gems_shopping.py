"""
보석 쇼핑
"""


def insert_gem_of_end_number(gems, gems_dict, end_number):
    # 현재 끝 진열대 번호에 해당하는 보석을
    # gems_dict에 추가한다.
    if gems[end_number] in gems_dict:
        # 기존에 해당 보석의 종류가 존재했으면 갯수만 1 증가시키고,
        gems_dict[gems[end_number]] += 1
    else:
        # 아예 없었으면 새로 추가한다.
        gems_dict[gems[end_number]] = 1


def remove_gem_of_start_number(gems, gems_dict, start_number):
    # 현재 시작 진열대 번호에 해당하는 보석이
    # gems_dict에 몇 개 있는지 확인한다.
    if gems_dict[gems[start_number]] == 1:
        # 만약 한 개만 있으면 아예 지워버리고,
        del gems_dict[gems[start_number]]
    elif gems_dict[gems[start_number]] >= 2:
        # 2개 이상 있으면 갯수를 1 감소시킨다.
        gems_dict[gems[start_number]] -= 1


def solution(gems):
    answer = []

    # 중복을 제거한 후의 길이를 측정하여
    # 모든 종류의 보석의 갯수를 구한다.
    number_of_all_kinds_of_gems = len(set(gems))

    # 전체 보석들의 끝 진열대 번호를 구한다.
    total_end_number = len(gems)

    # 리스트의 첫 번째 원소의 인덱스는 0이지만,
    # 문제의 첫 번째 진열대 번호는 1이므로
    # 이를 맞추기 위해 0 번째 인덱스에 의미없는 값을 넣는다.
    gems.insert(0, 0)

    # 현재 구간에 포함되어있는 보석들의 종류와,
    # 각 보석들의 갯수를 저장할 dictionary 선언
    gems_dict = dict()

    # 조건에 만족하는 구간들의
    # (구간의 길이, [시작 진열대 번호, 끝 진열대 번호]) 를 담을 리스트
    length_and_start_number_of_sections = []

    # 검사하는 시작 진열대 번호
    start_number = 1
    # 검사하는 끝 진열대 번호
    end_number = 1

    # 일단 시작 조건에서 무조건 포함되어있는
    # 진열대 번호 1번의 보석을
    # gems_dict에 추가한다.
    gems_dict[gems[start_number]] = 1

    while True:

        if end_number == total_end_number \
                and len(gems_dict) < number_of_all_kinds_of_gems:
            # 검사하는 끝 번호가 진열대에서 마지막 번호이고,
            # 현재 구간에 포함된 보석 종류의 수가 전체 보석의 종류의 수보다 작으면
            # 더 이상 전체 보석의 종류를 모두 1가지 이상씩 가질 수 없으므로, 검사를 끝낸다.
            break

        # 현재 gems_dict의 길이는
        # 현재 구간에 있는 보석들의 종류의 수 이다.
        # 이 값과 모든 보석의 종류의 수(number_of_all_kinds_of_gems)를 비교한다.
        if len(gems_dict) == number_of_all_kinds_of_gems:
            # 같으면 문제의 조건에 만족하므로
            # (현재 구간의 길이, [시작번호, 끝 번호])를
            # length_and_start_end_number_of_sections에 추가한다.
            length_and_start_number_of_sections.append(
                (end_number - start_number + 1, [start_number, end_number]))
            # 그리고 최소길이의 구간을 구하기 위해
            # start_number에 있던 보석을 gems_dict에서 한 개 제거하고,
            # start_number의 값을 1 증가시켜본다.
            remove_gem_of_start_number(gems, gems_dict, start_number)
            start_number += 1

        elif len(gems_dict) < number_of_all_kinds_of_gems:
            # 현재 구간에서의 보석의 종류의 수가 더 작으면,
            # end_number의 값을 1 증가시키고,
            # end_number에 있는 보석을 gems_dict에 추가한다.
            end_number += 1
            insert_gem_of_end_number(gems, gems_dict, end_number)

    # 1. 구간 길이를 기준으로 오름차순으로 정렬.
    # 2. 구간 길이가 같으면 시작 진열대 번호를 기준으로 오름차순으로 정렬.
    length_and_start_number_of_sections.sort(key=lambda x: (x[0], x[1][0]))

    # 답은 가장 구간 길이가 짧고, 구간 길이가 같을 경우 시작 진열대 번호가 가장 낮은 구간
    answer = length_and_start_number_of_sections[0][1]
    return answer
