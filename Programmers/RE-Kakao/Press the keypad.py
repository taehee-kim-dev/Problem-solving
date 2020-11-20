"""
2020 카카오 인턴십
키패드 누르기
"""


def solution(numbers, hand):
    answer = ''

    phone_map = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        0: (3, 1)
    }

    current_left_hand_position = (3, 0)
    current_right_hand_position = (3, 2)

    def get_diff(current_hand_position, number):
        x_diff = abs(current_hand_position[1] - phone_map[number][1])
        y_diff = abs(current_hand_position[0] - phone_map[number][0])
        return x_diff + y_diff

    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            current_left_hand_position = phone_map[num]
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            current_right_hand_position = phone_map[num]
        else:
            diff_left_hand = get_diff(current_left_hand_position, num)
            diff_right_hand = get_diff(current_right_hand_position, num)

            if diff_left_hand == diff_right_hand:
                if hand == 'right':
                    answer += 'R'
                    current_right_hand_position = phone_map[num]
                else:
                    answer += 'L'
                    current_left_hand_position = phone_map[num]
            elif diff_left_hand < diff_right_hand:
                answer += 'L'
                current_left_hand_position = phone_map[num]
            else:
                answer += 'R'
                current_right_hand_position = phone_map[num]
    return answer


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
# "LRLLLRLLRRL"
