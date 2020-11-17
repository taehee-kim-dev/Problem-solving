import sys
sys.setrecursionlimit(10000)

"""
섬의 개수
한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 하나의 섬
총 섬의 개수는?
"""

'''
왼쪽 위 블록부터 차례대로 블록들을 방문한다.
방문한 모든 블록은 방문했음을 표시한다.

방문한 블록에서 자신이 '1'이면, 섬이다. 총 섬의 개수 값을 1 증가시킨다. 
상, 하, 좌, 우, 대각선의 블록들을 검사한다.
'1'인 값이 있으면 같은 섬이다. 
그 섬 블록으로 이동한다.

다시 그 섬에서 상, 하, 좌, 우, 대각선의 블록들을 검사한다.
'1'인 값이 있으면 같은 섬이다.
그 섬 블록으로 이동한다.

다시 그 섬에서 상, 하, 좌, 우, 대각선의 블록들을 검사한다.
어느 블록에도 '1'인 값이 없다면, 해당 섬은 거기까지 연결되어 있는 것이다.

왼쪽 위 블록부터 차례대로 검사하여 방문하지 않은 블록에 간다.
거기서부터 다시 같은 과정을 반복한다.

모든 블록이 방문되어서 더이상 방문할 블록이 없으면 끝이다.
'''

total_island_count = 0


def check_same_island(row_index_to_check, col_index_to_check):
    global input_map
    # 검사하는 블록의 값이 '1'이 아니면, 같은 섬이 아니다.

    if input_map[row_index_to_check][col_index_to_check] != '1':
        return

    # 검사하는 블록의 값이 '1'이고 방문을 했으므로, 방문 표시를 한다.
    input_map[row_index_to_check][col_index_to_check] = 'v'

    # 상, 하, 좌, 우, 대각선의 블록들을 검사한다.
    # '1'인 값이 있으면 같은 섬이다.

    # 상, 하, 좌, 우 이동

    # 위쪽
    # 유효성 검사
    if 0 <= row_index_to_check - 1:
        # 위의 블록으로 이동
        check_same_island(row_index_to_check - 1, col_index_to_check)

    # 아래쪽
    # 유효성 검사
    if row_index_to_check + 1 < height:
        # 아래의 블록으로 이동
        check_same_island(row_index_to_check + 1, col_index_to_check)

    # 왼쪽
    # 유효성 검사
    if 0 <= col_index_to_check - 1:
        # 왼쪽 블록으로 이동
        check_same_island(row_index_to_check, col_index_to_check - 1)

    # 오른쪽
    # 유효성 검사
    if col_index_to_check + 1 < width:
        # 오른쪽 블록으로 이동
        check_same_island(row_index_to_check, col_index_to_check + 1)

    # 대각선 이동

    # 왼쪽 위 대각선
    if 0 <= col_index_to_check - 1 < width \
            and 0 <= row_index_to_check - 1 < height:
        # 이동
        check_same_island(row_index_to_check - 1, col_index_to_check - 1)

    # 오른쪽 위 대각선
    if 0 <= col_index_to_check + 1 < width \
            and 0 <= row_index_to_check - 1 < height:
        # 이동
        check_same_island(row_index_to_check - 1, col_index_to_check + 1)

    # 왼쪽 아래 대각선
    if 0 <= col_index_to_check - 1 < width \
            and 0 <= row_index_to_check + 1 < height:
        # 이동
        check_same_island(row_index_to_check + 1, col_index_to_check - 1)

    # 오른쪽 아래 대각선
    if 0 <= col_index_to_check + 1 < width \
            and 0 <= row_index_to_check + 1 < height:
        # 이동
        check_same_island(row_index_to_check + 1, col_index_to_check + 1)


def solution():
    global width, height, total_island_count, input_map

    # 왼쪽 위부터 차례대로 블록들 검사
    for row_index in range(height):
        for col_index in range(width):
            # 블록의 값이 '1'이라면, 새로운 섬이다.
            if input_map[row_index][col_index] == '1':
                # 전체 섬의 개수 값을 1 증가시킨다.
                total_island_count += 1
                # 현재 이 블록과 연결되어있는 같은 섬의 블록들을 찾는다.
                check_same_island(row_index, col_index)
                # 이 줄로 왔다면, 위의 섬과 연결되어있는 섬들은 모두 체크된 것이다.
                # 다음 새로운 섬을 찾는다.


# 1 <= width, height <= 50
width, height = map(int, input().split(' '))
input_map = []

while not (width == 0 and height == 0):
    input_map = []

    for row in range(height):
        input_map.append(list(input().split(' ')))

    solution()
    print(total_island_count)
    total_island_count = 0
    width, height = map(int, input().split(' '))
