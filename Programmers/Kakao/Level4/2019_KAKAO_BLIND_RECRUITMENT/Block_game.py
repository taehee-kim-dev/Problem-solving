"""
블록게임

빨간색 블록의 세 번째, 네 번째 케이스
노란색 블록의 두 번째, 세 번째 케이스
하늘색 블록의 첫 번째 케이스

들만 없앨 수 있다.
"""


# 빨간 블록 세 번째 케이스
def red_third_case(check_start_row, check_start_col, board, block_number, N):
    # 왼쪽에서 오른쪽으로, 위에서 아래로 검사하므로,
    # 현재 이 블록을 처음 찾은 위치를 포함하여
    # 오른쪽으로 세 칸, 아래쪽으로 두 칸의 직사각형 공간이 보드상에 존재하는지 먼저 확인한다.
    for row in range(check_start_row, check_start_row + 2):
        for col in range(check_start_col, check_start_col + 3):
            if not (0 <= row <= N - 1 and 0 <= col <= N - 1):
                return False

    # 빨간 블록 세 번째 케이스의 형태이다.
    red_third_block_with_black_blocks = [
        [block_number, -2, -2],
        [block_number, block_number, block_number]
    ]

    # 현재 검사하는 위치의 블록이 빨간 블록 세 번째 케이스의 형태인지 확인한다.
    for row in range(2):
        for col in range(3):
            if board[check_start_row + row][check_start_col + col] \
                    != red_third_block_with_black_blocks[row][col]:
                return False

    # 형태가 맞다면, 검은 블록을 포함하여 해당 블록을 모두 0으로 삭제한다.
    for row in range(check_start_row, check_start_row + 2):
        for col in range(check_start_col, check_start_col + 3):
            board[row][col] = 0

    return True


# 빨간 블록 네 번째 케이스
def red_fourth_case(check_start_row, check_start_col, board, block_number, N):
    # 왼쪽에서 오른쪽으로, 위에서 아래로 검사하므로,
    # 현재 이 블록을 처음 찾은 위치를 포함하여
    # 왼쪽으로 두 칸, 아래쪽으로 세 칸의 공간이 보드상에 존재하는지 먼저 확인한다.
    for row in range(check_start_row, check_start_row + 3):
        for col in range(check_start_col, check_start_col - 2, -1):
            if not (0 <= row <= N - 1 and 0 <= col <= N - 1):
                return False

    # 빨간 블록 네 번째 케이스의 형태이다.
    red_fourth_block_with_black_blocks = [
        [-2, block_number],
        [-2, block_number],
        [block_number, block_number]
    ]

    # 현재 검사하는 위치의 블록이 빨간 블록 네 번째 케이스의 형태인지 확인한다.
    for row in range(3):
        for col in range(2):
            if board[check_start_row + row][check_start_col - 1 + col] \
                    != red_fourth_block_with_black_blocks[row][col]:
                return False

    # 형태가 맞다면, 검은 블록을 포함하여 해당 블록을 모두 0으로 삭제한다.
    for row in range(check_start_row, check_start_row + 3):
        for col in range(check_start_col, check_start_col - 2, -1):
            board[row][col] = 0

    return True


# 노란 블록 두 번째 케이스
def yellow_second_case(check_start_row, check_start_col, board, block_number, N):
    # 왼쪽에서 오른쪽으로, 위에서 아래로 검사하므로,
    # 현재 이 블록을 처음 찾은 위치를 포함하여
    # 오른쪽으로 두 칸, 아래쪽으로 세 칸의 공간이 보드상에 존재하는지 먼저 확인한다.
    for row in range(check_start_row, check_start_row + 3):
        for col in range(check_start_col, check_start_col + 2):
            if not (0 <= row <= N - 1 and 0 <= col <= N - 1):
                return False

    # 노란 블록 두 번째 케이스의 형태이다.
    yellow_second_block_with_black_blocks = [
        [block_number, -2],
        [block_number, -2],
        [block_number, block_number]
    ]

    # 현재 검사하는 위치의 블록이 노란 블록 두 번째 케이스의 형태인지 확인한다.
    for row in range(3):
        for col in range(2):
            if board[check_start_row + row][check_start_col + col] \
                    != yellow_second_block_with_black_blocks[row][col]:
                return False

    # 형태가 맞다면, 검은 블록을 포함하여 해당 블록을 모두 0으로 삭제한다.
    for row in range(check_start_row, check_start_row + 3):
        for col in range(check_start_col, check_start_col + 2):
            board[row][col] = 0

    return True


# 노란 블록 세 번째 케이스
def yellow_third_case(check_start_row, check_start_col, board, block_number, N):
    # 왼쪽에서 오른쪽으로, 위에서 아래로 검사하므로,
    # 현재 이 블록을 처음 찾은 위치를 포함하여
    # 왼쪽으로 세 칸, 아래쪽으로 두 칸의 공간이 보드상에 존재하는지 먼저 확인한다.
    for row in range(check_start_row, check_start_row + 2):
        for col in range(check_start_col, check_start_col - 3, -1):
            if not (0 <= row <= N - 1 and 0 <= col <= N - 1):
                return False

    # 노란 블록 세 번째 케이스의 형태이다.
    yellow_third_block_with_black_blocks = [
        [-2, -2, block_number],
        [block_number, block_number, block_number]
    ]

    # 현재 검사하는 위치의 블록이 노란 블록 세 번째 케이스의 형태인지 확인한다.
    for row in range(2):
        for col in range(3):
            if board[check_start_row + row][check_start_col - 2 + col] \
                    != yellow_third_block_with_black_blocks[row][col]:
                return False

    # 형태가 맞다면, 검은 블록을 포함하여 해당 블록을 모두 0으로 삭제한다.
    for row in range(check_start_row, check_start_row + 2):
        for col in range(check_start_col, check_start_col - 3, -1):
            board[row][col] = 0

    return True


# 하늘색 블록 첫 번째 케이스
def skyblue_first_case(check_start_row, check_start_col, board, block_number, N):
    # 왼쪽에서 오른쪽으로, 위에서 아래로 검사하므로,
    # 현재 이 블록을 처음 찾은 위치를 포함하여
    # 왼쪽 한 칸, 오른쪽 한 칸, 아래로 두 칸의 공간이 보드상에 존재하는지 먼저 확인한다.
    for row in range(check_start_row, check_start_row + 2):
        for col in range(check_start_col - 1, check_start_col - 1 + 3):
            if not (0 <= row <= N - 1 and 0 <= col <= N - 1):
                return False

    # 하늘색 블록 첫 번째 케이스의 형태이다.
    skyblue_first_block_with_black_blocks = [
        [-2, block_number, -2],
        [block_number, block_number, block_number]
    ]

    # 현재 검사하는 위치의 블록이 하늘색 블록 첫 번째 케이스의 형태인지 확인한다.
    for row in range(2):
        for col in range(3):
            if board[check_start_row + row][check_start_col - 1 + col] \
                    != skyblue_first_block_with_black_blocks[row][col]:
                return False

    # 형태가 맞다면, 검은 블록을 포함하여 해당 블록을 모두 0으로 삭제한다.
    for row in range(check_start_row, check_start_row + 2):
        for col in range(check_start_col - 1, check_start_col - 1 + 3):
            board[row][col] = 0

    return True


# 현재 존재하고 검은 블록을 쌓을 수 있는 블록들의 위로 검은 블록을 2개씩 쌓는 함수.
def drop_black_blocks(N, board):
    # 맨 왼쪽 열부터 맨 오른쪽 열까지 차례대로 실행
    for col in range(N):
        row = -1
        while True:
            # 맨 위의 행 부터 차례대로 한칸씩 내려온다.
            # 블록을 만날 때 까지.
            row += 1
            # 만약 끝행까지 검사했으면 다음 열을 검사한다.
            if row == N:
                break
            # 현재 검사하는 보드 위의 칸
            checking_block = board[row][col]
            # 검은블록의 값은 -2
            # 만약 현재 검사하는 보드위가 검은블록이나 빈칸이라면 무시하고
            # 한 칸 아래 행으로 내려간다.
            if checking_block == 0 or checking_block == -2:
                continue
            # 만약 현재 검사하는 보드위가 어떤 블록으로 채워져있다면
            if checking_block > 0:
                # 그 블록 바로 위의 칸이 비어있으면 검은블록으로 채워준다.
                if 0 <= row - 1 and board[row - 1][col] == 0:
                    board[row - 1][col] = -2
                # 그 블록 바로 위 두 번째 칸이 비어있으면 검은블록으로 채워준다.
                if 0 <= row - 2 and board[row - 2][col] == 0:
                    board[row - 2][col] = -2

                # 제일 위에 있는 블록 위에 검은 블록 두 개를 떨어뜨렸으므로
                # 다음 열에 작업하러 간다.
                break


def solution(board):
    # 총 삭제된 블록의 수
    number_of_deleted_blocks = 0
    # board 한 변의 길이
    N = len(board)
    # 맨 위의 행부터 맨 아래의 행까지 차례대로 검사
    for row in range(N):
        while True:
            # 왼쪽에서 오른쪽으로 검사하기 때문에,
            # B보다 왼쪽에서 먼저 탐지되는 A블록이
            # B블록 아래에 있어서 원래는 삭제가 불가능했지만,
            # B블록이 삭제되고 나서는 A블록이 삭제가 가능할 수도 있다.
            # 따라서, 한 행에서 더이상 삭제가능한 블록이 안 나올 때 까지
            # 해당 행의 삭제 과정을 반복한다.

            # 이 행에서 새롭게 삭제된 블록의 수
            number_of_new_deleted_blocks = 0
            # 맨 왼쪽의 열부터 맨 오른쪽의 열까지 차례대로 검사
            for col in range(N):
                # 현재 존재하고, 검은 블록을 쌓을 수 있는 블록들의 위로 검은 블록을 2개씩 쌓는다.
                # 어떤 블록을 삭제했을 때, 해당 블록이 차지하고 있던 자리에
                # 검은 블록을 쌓을 수 있으므로
                # 매 열을 검사할 때 마다 2개씩 쌓는다.
                drop_black_blocks(N, board)
                if board[row][col] > 0:
                    # 블록이 있다면
                    # 현재 검사하는 블록의 번호를 저장
                    block_number = board[row][col]

                    # 빨간색 블록의 세 번째 케이스이고 검은색 블록으로 채워져 있으면 검은색 블록과 함께 삭제
                    # 빨간색 블록의 네 번째 케이스이고 검은색 블록으로 채워져 있으면 검은색 블록과 함께 삭제

                    # 노란색 블록의 두 번째 케이스이고 검은색 블록으로 채워져 있으면 검은색 블록과 함께 삭제
                    # 노란색 블록의 세 번째 케이스이고 검은색 블록으로 채워져 있으면 검은색 블록과 함께 삭제

                    # 하늘색 블록의 첫 번째 케이스이고 이고 검은색 블록으로 채워져 있으면 검은색 블록과 함께 삭제
                    if red_third_case(row, col, board, block_number, N) \
                            or red_fourth_case(row, col, board, block_number, N) \
                            or yellow_second_case(row, col, board, block_number, N) \
                            or yellow_third_case(row, col, board, block_number, N) \
                            or skyblue_first_case(row, col, board, block_number, N):
                        # 어느 하나의 경우라도 해당돼서 삭제했다면
                        # 현재 이 행에서 새롭게 삭제한 블록의 수를 1 증가시키고,
                        number_of_new_deleted_blocks += 1
                        # 총 삭제한 블록의 수를 1 증가시킨다.
                        number_of_deleted_blocks += 1

            # 만약 이 행에서 더이상 삭제된 블록이 없으면
            # 다음 행으로 내려온다.
            if number_of_new_deleted_blocks == 0:
                break

    # 총 삭제된 블록의 수를 반환한다.
    return number_of_deleted_blocks


print(solution([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 4, 0, 0, 0],
    [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
    [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]
]))
# 2

print(solution([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 9, 0, 8, 0, 4, 0, 0, 0, 0],
    [0, 7, 9, 8, 8, 8, 4, 0, 0, 0, 0],
    [0, 7, 9, 9, 3, 4, 4, 0, 0, 0, 0],
    [7, 7, 0, 2, 3, 0, 0, 0, 5, 5, 0],
    [1, 2, 2, 2, 3, 3, 0, 0, 0, 5, 0],
    [1, 1, 1, 6, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 6, 6, 6, 0, 0, 0, 0, 0, 0]
]))
# 8
