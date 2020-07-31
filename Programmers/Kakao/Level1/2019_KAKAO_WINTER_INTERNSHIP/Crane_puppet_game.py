"""
2019 카카오 개발자 겨울 인턴십
크레인 인형뽑기 게임
"""


def solution(board, moves):
    answer = 0
    basket = []
    total_floor = len(board)

    for x_position in moves:
        x_position_index = x_position - 1
        for y_position_index in range(total_floor):
            current_doll = board[y_position_index][x_position_index]
            if current_doll != 0:
                board[y_position_index][x_position_index] = 0
                if len(basket) >= 1 and basket[-1] == current_doll:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(current_doll)
                break
    return answer


print(solution(
    [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3],
        [0, 2, 5, 0, 1],
        [4, 2, 4, 4, 2],
        [3, 5, 1, 3, 1]
    ],
    [1, 5, 3, 5, 1, 2, 1, 4]))
