from queue import Queue

"""
경주로 건설
"""

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)

SET_STRAIGHT_ROAD = 'set_straight_road'
SET_CORNER = 'set_corner'

"""
코너의 갯수가 고정된 상황에서,
최소비용으로 경주로를 건설하려면,
직선도로를 가장 적게 써야한다.
BFS로 최단거리 경로를 찾는다고 할 때,
거리를 총 쓰인 직선도로 + 코너의 갯수로 놓는다.
이 거리의 정의로 최단거리의 경로를 얻으면,
코너의 갯수는 어차피 고정되어 있으므로
직선도로를 가장 적게 쓴 거리가 되고
이는 해당 고정된 코너의 갯수를 가진 경로 중에서 
최단거리인 경로, 즉 최소비용인 경로가 된다. 
"""


def find_next_position(position_to_check, board, visited_positions):
    """
    position_to_check =
    (현재 좌표(x좌표, y좌표), 해당 좌표에서의 경로의 방향, 해당 좌표까지 쓰인 직진도로 또는 코너의 갯수, 해당 좌표까지 쓰인 코너의 갯수, 현재 체크중인 코너의 갯수, 직전 작업)
    """
    current_position, current_direction, number_of_current_straight_roads_or_corners, \
        number_of_current_corners, number_of_corners_to_check, before_task \
        = position_to_check

    possible_next_positions = []

    next_directions = [RIGHT, LEFT, UP, DOWN]
    # 다음 방문 위치 구하기
    for next_direction in next_directions:

        # 다음 진행 방향이 역방향이면 안된다.
        # 왜냐하면 이미 역방향으로는 직선도로가 놓여있기 때문.
        if next_direction == (-1 * current_direction[0], -1 * current_direction[1]):
            continue

        # 다음 방문할 위치
        next_position = (current_position[0] + next_direction[0], current_position[1] + next_direction[1])

        # 다음 방문할 위치가 벽, 범위 밖, 방문했던 곳이 아니어야 한다.
        """
        방문했던 곳이라는 의미는 이미 더 짧은 거리를 가진 경로가 
        이미 그 자리에서 가능한 모든 작업들(직선도로 또는 코너 설치)을 했다는 것이다.
        따라서 그 방향으로 직진 또는 코너를 설치하는 것은, 뒤늦게 그 자리에서 위의 작업들을 하겠다는 것이므로,
        최단경로를 찾고있는 현재 함수에서는 옳지 않다.
        """
        if board[next_position[0]][next_position[1]] == 1 or next_position in visited_positions:
            continue

        # 현재 방향과 다음 방향이 같다면, 직선으로 나아간다는 것.
        if current_direction == next_direction:
            # 직선 방향으로 나아갈 경우
            possible_next_positions.append((next_position, current_direction,
                                            number_of_current_straight_roads_or_corners + 1, number_of_current_corners,
                                            number_of_corners_to_check, SET_STRAIGHT_ROAD))
        else:
            # 현재 방향과 다음 방향이 같지 않다면,
            # 현재 칸에서 90도로 회전한다는 것.
            # 즉, 현재 칸에서 코너가 만들어 진다는 것.
            if number_of_current_corners == number_of_corners_to_check:
                # 이미 최대 가능 코너 갯수를 다 썼다면,
                # 코너를 더이상 만들 수 없다.
                continue
            elif before_task != SET_CORNER:
                # 아직 최대 가능 코너 갯수를 다 쓰지 않았다면,
                # 회전시킬 수 있다.
                # 단, 직전 작업이 회전이 아니었어야 한다.
                # 다음 위치는 현재 위치랑 같다.
                possible_next_positions.append((current_position, next_direction,
                                                number_of_current_straight_roads_or_corners + 1,
                                                number_of_current_corners + 1, number_of_corners_to_check, SET_CORNER))
    visited_positions.append(current_position)
    return possible_next_positions


def solution(board):
    N = len(board)

    """
    계산 쉽게 하기 위해 바깥 부분을 1로 둘러쌈
    출발점 (1, 1) -> 도착점 (N, N)
    """
    board_extension = [[1 for col in range(N + 2)] for row in range(N + 2)]

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                board_extension[row + 1][col + 1] = 0

    board = board_extension

    all_costs = []

    # 존재 가능한 코너의 갯수는 1개 이상 N * N개 이하
    for number_of_corners_to_check in range(1, (N * N) + 1):
        queue = Queue()
        # (현재 좌표(x좌표, y좌표), 해당 좌표에서의 경로의 방향, 해당 좌표까지 쓰인 직진도로 또는 코너의 갯수, 해당 좌표까지 쓰인 코너의 갯수, 현재 체크중인 코너의 갯수, 직전 작업)
        queue.put(((1, 2), RIGHT, 1, 0, number_of_corners_to_check, SET_STRAIGHT_ROAD))
        queue.put(((2, 1), DOWN, 1, 0, number_of_corners_to_check, SET_STRAIGHT_ROAD))

        visited_positions = [(1, 1)]

        while not queue.empty():
            found_min_number_of_constructor_case = False
            position_to_check = queue.get()
            next_positions = find_next_position(position_to_check, board, visited_positions)
            for next_position in next_positions:
                if next_position[0] == (N, N) and next_position[3] == number_of_corners_to_check:
                    # 목적지 도착 시, 해당 정보가 검사하고있던 코너 갯수 조건에서 최소 비용.
                    # 현재 비용 계산해서 저장
                    count_of_straight_road = next_position[2] - number_of_corners_to_check
                    count_of_corner = number_of_corners_to_check
                    current_total_cost = (100 * count_of_straight_road) + (500 * count_of_corner)
                    all_costs.append(current_total_cost)
                    found_min_number_of_constructor_case = True
                    break
                queue.put(next_position)
            if found_min_number_of_constructor_case:
                break
    return sorted(all_costs)[0]


print(solution([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]))
# 900

print(solution([
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0]
]))
# 3800

print(solution([
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 0]
]))
# 2100

print(solution([
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0]
]))
# 3200
