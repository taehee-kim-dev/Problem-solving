import itertools

"""
KAKAO Level2
후보키
"""

attribute_list = []

candidate_key_count = 0


# 한 attribute에 해당하는 모든 value들을 검사하여
# 해당 attribute가 유일성을 갖는지 검사
def is_unique(attribute):

    attribute_list_size = len(attribute)
    attribute_set_size = len(set(attribute))

    return attribute_list_size == attribute_set_size


# 한 attribute에 해당하는 value들을 각 리스트로 묶음
def relation_to_attribute_list(relation):
    for col_index in range(len(relation[0])):
        attribute = []
        for row_index in range(len(relation)):
            attribute.append(relation[row_index][col_index])
        attribute_list.append(attribute)


# set 내에 있는 인덱스들에 해당하는 속성들의 각 value에 해당하는 문자열 값 들을 합치는 함수
def combine_attribute(attribute_index_set):
    attribute = []
    combined_attribute = []
    for attribute_index in attribute_index_set:
        attribute.append(attribute_list[attribute_index])

    for row_index in range(len(attribute[0])):
        row_data = ''
        for attribute_list_2 in attribute:
            row_data += attribute_list_2[row_index]

        combined_attribute.append(row_data)

    return combined_attribute


def solution(relation):
    global candidate_key_count

    # row별 리스트를 attribute별 리스트로 전환
    relation_to_attribute_list(relation)

    # 총 속성의 개수
    attribute_size = len(attribute_list)
    # 각 속성을 0부터 총 속성의 개수 -1 까지 인덱스를 매김
    attribute_index_list = list(range(attribute_size))

    # 속성들의 인덱스들을 선택할 수 있는 모든 조합(Combination)을 구해서 set화 시키고, 이들을 하나의 리스트에 담음.
    attribute_index_combination_set_list = []
    for size in range(1, attribute_size + 1):
        attribute_index_combination_set_list.extend(list(map(set, itertools.combinations(attribute_index_list, size))))

    # Combination들을 담은 리스트의 인덱스를 0부터 검사
    for set_list_index in range(len(attribute_index_combination_set_list)):
        # 현재 인덱스에 해당하는 값이 'X'가 아닐 경우,
        if attribute_index_combination_set_list[set_list_index] != 'X':
            # 해당 조합에서 선택된 인덱스의 속성에 해당하는 각 행의 value들을 문자열 합치기로 합친 리스트 결과를 받음.
            # 조합에서 1개만 선택된 경우는 그 1개의 속성 리스트가 그대로 반환됨.
            combined_attribute_list = combine_attribute(attribute_index_combination_set_list[set_list_index])

            # 위에서 받은 합쳐진 속성 조합이 유일성을 갖는지 검사.
            if is_unique(combined_attribute_list):
                # 유일성을 갖는다면 정답을 1 증가시킴
                candidate_key_count += 1
                # 지금 선택된 조합 인덱스 이후의 값들 중,
                # 지금 선택된 조합을 포함하는 다른 모든 조합들을 'X'로 바꿈. 최소성을 가져야 하기 때문.
                for set_list_index_2 in range(set_list_index + 1, len(attribute_index_combination_set_list)):
                    if attribute_index_combination_set_list[set_list_index].issubset(attribute_index_combination_set_list[set_list_index_2]):
                        attribute_index_combination_set_list[set_list_index_2] = 'X'

    answer = candidate_key_count

    return answer
