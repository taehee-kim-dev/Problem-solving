"""
징검다리 건너기
"""


# 매개변수로 받은 number_of_people 수 만큼의 모든 사람들이
# 매개변수로 받은 징검다리를 건널 수 있는가?
def can_cross_stones(stones, number_of_people, k):
    # 사람들이 건너고 있는 중간에 0의 디딤돌이 연속으로 k개 이상이 되면,
    # 그 이후의 사람들이 건널 수 없어, 모든 사람들이 징검다리를 건널 수 없다.
    # 하지만, 모든 사람들이 건너고 나서 0의 디딤돌이 연속으로 k개 이상이 되는것은,
    # 이미 모든 사람들이 건넌 이후이므로 상관없다.

    # 사람들이 건너고 있는 동안에 체크한 연속된 0의 디딤돌의 수
    zeros_continuous_count_while_crossing = 0
    # 디딤돌을 하나씩 검사한다.
    for stone in stones:
        # 디딤돌의 숫자가 건너려는 사람의 수보다 작으면
        # 사람들이 이 디딤돌을 건너고 있는 중간에
        # 이 돌의 숫자는 0이된다.
        if stone < number_of_people:
            # 사람들이 건너고 있는 동안에 체크한 연속된 0의 디딤돌의 수 1 증가
            zeros_continuous_count_while_crossing += 1
            # 만약 현재까지 체크한 연속된 0의 디딤돌의 갯수가 k이상이면
            # number_of_people의 사람들은 이 징검다리를 건널 수 없다.
            if zeros_continuous_count_while_crossing >= k:
                return False
        else:
            # 디딤돌의 숫자가 건너려는 사람의 수보다 크거나 같으면,
            # 해당 수의 사람들이 모두 건너는 중간에 이 디딤돌은 0이 되지 않는다.
            # 디딤돌의 숫자가 건너려는 사람의 수와 같다면
            # 마지막 순서의 사람이 이 돌을 밟으면서 건넜을 때 0이 되므로,
            # 결국 모든 사람들이 건너고 나서 0이 되는 것이다.
            # 따라서 사람들이 건너고 있는 중간에는 0이 아니므로,
            # 위에서 세고있던 zeros_continuous_count_while_crossing를
            # 0으로 초기화해야 한다.
            zeros_continuous_count_while_crossing = 0

    # for문을 무사히 빠져나오면,
    # number_of_people 수의 사람들이 이 징검다리를 건널 수 있다.
    return True


def solution(stones, k):
    # 징검다리를 건널 수 있는 최소 인원 수
    min_number_of_people_for_test = 1
    # 징검다리를 건널 수 있는 최대 인원 수
    max_number_of_people_for_test = 200000000

    # 이분탐색
    # 최소인원과 최소인원의 차이가 1 이하일 때 까지 탐색
    while max_number_of_people_for_test - min_number_of_people_for_test > 1:
        # 최소 인원과 최소 인원의 중간값을 구한다. (소수점 버림)
        mid_number_of_people_for_test = (min_number_of_people_for_test + max_number_of_people_for_test) // 2
        if can_cross_stones(stones, mid_number_of_people_for_test, k):
            # 중간값의 인원으로 건널 수 있으면,
            # 징검다리를 건널 수 있는 최대 인원수 값은 이 중간값 이상의 범위에 있다.
            # 따라서 최소 인원을 이 중간값으로 설정한다.
            min_number_of_people_for_test = mid_number_of_people_for_test
        else:
            # 중간값의 인원으로 건널 수 없으면,
            # 중간값의 인원보다 작은 범위에 최대값이 존재한다.
            # 최댓값을 중간값으로 설정한다.
            max_number_of_people_for_test = mid_number_of_people_for_test

    # 그러면 무조건 최솟값이 징검다리를 건널 수 있는 최대 인원이 된다.
    return min_number_of_people_for_test
