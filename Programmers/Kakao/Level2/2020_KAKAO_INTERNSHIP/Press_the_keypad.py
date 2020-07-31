"""
2020 카카오 인턴십
키패드 누르기
"""

def solution(numbers, hand):
    answer = ''

    current_left_hand_number = '*'
    current_right_hand_number = '#'

    number_map_dict = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],

        4: [1, 0],
        5: [1, 1],
        6: [1, 2],

        7: [2, 0],
        8: [2, 1],
        9: [2, 2],

        '*': [3, 0],
        0: [3, 1],
        '#': [3, 2],
    }

    for current_number in numbers:
        if current_number == 1 or current_number == 4 or current_number == 7:
            answer += 'L'
            current_left_hand_number = current_number
        elif current_number == 3 or current_number == 6 or current_number == 9:
            answer += 'R'
            current_right_hand_number = current_number
        else:
            left_hand_distance = \
                abs(number_map_dict[current_number][0] - number_map_dict[current_left_hand_number][0]) \
                + abs(number_map_dict[current_number][1] - number_map_dict[current_left_hand_number][1])

            right_hand_distance = \
                abs(number_map_dict[current_number][0] - number_map_dict[current_right_hand_number][0]) \
                + abs(number_map_dict[current_number][1] - number_map_dict[current_right_hand_number][1])

            if left_hand_distance == right_hand_distance:
                if hand == 'left':
                    answer += 'L'
                    current_left_hand_number = current_number
                else:
                    answer += 'R'
                    current_right_hand_number = current_number
            elif left_hand_distance < right_hand_distance:
                answer += 'L'
                current_left_hand_number = current_number
            else:
                answer += 'R'
                current_right_hand_number = current_number
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL")

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR")

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == "LLRLLRLLRL")
