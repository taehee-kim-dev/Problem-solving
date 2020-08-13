

def solution(input_str):
    # 정답 튜플을 담을 리스트
    answer = []

    # set형 문자열 input_str을 list화하여 저장할 list
    list_of_number = []

    # input_str집합의 원소들을 문자열로 가지는 리스트로 변환
    list_of_str_element_of_input_str = input_str[2:len(input_str) - 2].split("},{")

    # list_of_str_element_of_input_str의 각 문자열 원소들을 리스트화
    for element in list_of_str_element_of_input_str:
        list_of_number.append(list(map(int, element.split(','))))

    # 원소 list의 길이 순으로 정렬
    list_of_number.sort(key=len)

    # answer list에 없는 원소를 answer list의 맨 뒤에 추가
    for element in list_of_number:
        for number in element:
            if number not in answer:
                answer.append(number)

    return answer
