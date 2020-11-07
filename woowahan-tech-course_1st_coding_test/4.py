
def get_min_dist_in_x(current_cursor_position, next_number_to_delete, board, n):

    x_position_of_number_to_delete = 0
    for row_i in range(n):
        for col_i in range(n):
            if board[row_i][col_i] == next_number_to_delete:
                x_position_of_number_to_delete = col_i

    left_side_dist = 0
    right_side_dist = 0

    # 오른쪽으로 이동해본다.
    current_x = current_cursor_position[0]
    while current_x != x_position_of_number_to_delete:
        current_x += 1
        right_side_dist += 1
        if n - 1 < current_x:
            current_x = 0

    # 왼쪽으로 이동해본다.
    current_x = current_cursor_position[0]
    while current_x != x_position_of_number_to_delete:
        current_x -= 1
        left_side_dist += 1
        if current_x < 0:
            current_x = n - 1

    return min(left_side_dist, right_side_dist), x_position_of_number_to_delete


def get_min_dist_in_y(current_cursor_position, next_number_to_delete, board, n):

    y_position_of_number_to_delete = 0
    for row_i in range(n):
        for col_i in range(n):
            if board[row_i][col_i] == next_number_to_delete:
                y_position_of_number_to_delete = row_i


    down_side_dist = 0
    up_side_dist = 0

    # 아래쪽으로 이동해본다.
    current_y = current_cursor_position[1]
    while current_y != y_position_of_number_to_delete:
        current_y += 1
        down_side_dist += 1
        if n - 1 < current_y:
            current_y = 0

    # 위쪽으로 이동해본다.
    current_y = current_cursor_position[1]
    while current_y != y_position_of_number_to_delete:
        current_y -= 1
        up_side_dist += 1
        if current_y < 0:
            current_y = n - 1

    return min(up_side_dist, down_side_dist), y_position_of_number_to_delete


def solution(n, board):
    answer = 0

    current_cursor_position = (0, 0)
    for next_number_to_delete in range(1, ( n* *2) + 1):
        x_min, current_cursor_x_position = get_min_dist_in_x(current_cursor_position, next_number_to_delete, board, n)
        y_min, current_cursor_y_position = get_min_dist_in_y(current_cursor_position, next_number_to_delete, board, n)
        answer += (x_min + y_min + 1)
        current_cursor_position = (current_cursor_x_position, current_cursor_y_position)

    return answer


solution(3, [[3, 5, 6], [9, 2, 7], [4, 1, 8]])
