
def solution(n, horizontal):

    if n == 1:
        return [[0]]

    matrix = [[0 for _ in range(n)] for _ in range(n)]

    go_left_down = True
    row_i, col_i = 0, 1
    time_to_cross = 1
    is_time_to_cross_increasing = True
    current_time = 1
    matrix[row_i][col_i] = current_time
    while True:

        if go_left_down:
            for _ in range(time_to_cross):
                col_i -= 1
                row_i += 1
                current_time += 2
                matrix[row_i][col_i] = current_time
                go_left_down = False
            if is_time_to_cross_increasing:
                if time_to_cross < n - 1:
                    time_to_cross += 1
                    row_i += 1
                elif time_to_cross == n - 1:
                    is_time_to_cross_increasing = False
                    col_i += 1
                current_time += 1
                matrix[row_i][col_i] = current_time

            if not is_time_to_cross_increasing:
                time_to_cross -= 1
                if [row_i, col_i + 1] == [n - 1, n - 1]:
                    matrix[row_i][col_i + 1] = matrix[row_i][col_i] + 1
                    return matrix
        else:
            for _ in range(time_to_cross):
                col_i += 1
                row_i -= 1
                current_time += 2
                matrix[row_i][col_i] = current_time
                go_left_down = True
            if is_time_to_cross_increasing:
                if time_to_cross < n - 1:
                    time_to_cross += 1
                    col_i += 1
                elif time_to_cross == n - 1:
                    is_time_to_cross_increasing = False
                    row_i += 1
                current_time += 1
                matrix[row_i][col_i] = current_time



#print(solution(4, True))
"""
[
[0,1,8,9],
[3,6,11,20],
[4,13,18,21],
[15,16,23,24]
]
"""

print(solution(5, False))
"""
[
[0,3,4,15,16],
[1,6,13,18,31],
[8,11,20,29,32],
[9,22,27,34,39],
[24,25,36,37,40]
]
"""
