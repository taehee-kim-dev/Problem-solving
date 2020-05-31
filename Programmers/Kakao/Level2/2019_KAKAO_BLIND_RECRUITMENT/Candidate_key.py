import itertools

"""
KAKAO Level2
후보키
"""

attribute_list = []

candidate_key_count = 0


# 한 attribute의 value들을 검사하여
# 해당 attribute가 유일성을 갖는지 검사
def is_unique(attribute):

    attribute_list_size = len(attribute)
    attribute_set_size = len(set(attribute))

    return attribute_list_size == attribute_set_size


# attribute 들끼리 하나의 리스트로 묶음
def relation_to_attribute_list(relation):
    for col_index in range(len(relation[0])):
        attribute = []
        for row_index in range(len(relation)):
            attribute.append(relation[row_index][col_index])
        attribute_list.append(attribute)


# set 내에 있는 인덱스들에 해당하는 속성들을 합치는 함수
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

    relation_to_attribute_list(relation)

    attribute_size = len(attribute_list)
    attribute_index_list = list(range(attribute_size))

    attribute_index_combination_set_list = []
    for size in range(1, attribute_size + 1):
        attribute_index_combination_set_list.extend(list(map(set, itertools.combinations(attribute_index_list, size))))

    for set_list_index in range(len(attribute_index_combination_set_list)):
        if attribute_index_combination_set_list[set_list_index] != 'X':
            combined_attribute_list = combine_attribute(attribute_index_combination_set_list[set_list_index])

            if is_unique(combined_attribute_list):
                candidate_key_count += 1
                for set_list_index_2 in range(set_list_index + 1, len(attribute_index_combination_set_list)):
                    if attribute_index_combination_set_list[set_list_index].issubset(attribute_index_combination_set_list[set_list_index_2]):
                        attribute_index_combination_set_list[set_list_index_2] = 'X'

    answer = candidate_key_count

    return answer
