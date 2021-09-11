def solution(places):
    answer = []

    for place in places:
        answer_false_checked = False
        for row_index in range(0, 5):
            if answer_false_checked:
                break
            for col_index in range(0, 5):
                if (place[row_index][col_index] == 'P') and \
                        not (check_place_one_distance_cross_shape(place, row_index, col_index)
                             and check_place_two_distance_cross_shape(place, row_index, col_index)
                             and check_place_distance_right_down(place, row_index, col_index)
                             and check_place_distance_right_up(place, row_index, col_index)
                             and check_place_distance_left_up(place, row_index, col_index)
                             and check_place_distance_left_down(place, row_index, col_index)):
                    answer.append(0)
                    answer_false_checked = True
                    break
        if not answer_false_checked:
            answer.append(1)
    return answer


def check_place_one_distance_cross_shape(place, row_index, col_index):
    if (col_index - 1 >= 0 and place[row_index][col_index - 1] == 'P') \
            or (col_index + 1 <= 4 and place[row_index][col_index + 1] == 'P') \
            or (row_index - 1 >= 0 and place[row_index - 1][col_index] == 'P') \
            or (row_index + 1 <= 4 and place[row_index + 1][col_index] == 'P'):
        return False
    return True


def check_place_two_distance_cross_shape(place, row_index, col_index):
    if ((col_index - 2 >= 0 and place[row_index][col_index - 2] == 'P') and place[row_index][col_index - 1] != 'X') \
            or ((col_index + 2 <= 4 and place[row_index][col_index + 2] == 'P') and place[row_index][col_index + 1] != 'X') \
            or ((row_index - 2 >= 0 and place[row_index - 2][col_index] == 'P') and place[row_index - 1][col_index] != 'X') \
            or ((row_index + 2 <= 4 and place[row_index + 2][col_index] == 'P') and place[row_index + 1][col_index] != 'X'):
        return False
    return True


def check_place_distance_right_down(place, row_index, col_index):
    if (row_index + 1 <= 4 and col_index + 1 <= 4) and (place[row_index + 1][col_index + 1] == 'P'):
        if not ((place[row_index][col_index + 1] == 'X') and (place[row_index + 1][col_index] == 'X')):
            return False
    return True


def check_place_distance_right_up(place, row_index, col_index):
    if (row_index - 1 >= 0 and col_index + 1 <= 4) and (place[row_index - 1][col_index + 1] == 'P'):
        if not ((place[row_index][col_index + 1] == 'X') and (place[row_index - 1][col_index] == 'X')):
            return False
    return True


def check_place_distance_left_up(place, row_index, col_index):
    if (row_index - 1 >= 0 and col_index - 1 >= 0) and (place[row_index - 1][col_index - 1] == 'P'):
        if not ((place[row_index][col_index - 1] == 'X') and (place[row_index - 1][col_index] == 'X')):
            return False
    return True


def check_place_distance_left_down(place, row_index, col_index):
    if (row_index + 1 <= 4 and col_index - 1 >= 0) and (place[row_index + 1][col_index - 1] == 'P'):
        if not ((place[row_index][col_index - 1] == 'X') and (place[row_index + 1][col_index] == 'X')):
            return False
    return True


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
