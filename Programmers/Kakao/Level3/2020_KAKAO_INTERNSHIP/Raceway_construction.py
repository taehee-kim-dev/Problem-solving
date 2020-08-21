from queue import Queue

"""
경주로 건설
"""

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


def find_next_position(current_position, current_direction, count_of_current_straight_road_or_corner,
                       current_corner, corner_limit, board, visited_positions):

    possible_next_positions = []

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # 다음 방문 위치 구하기
    for direction in directions:

        # 다음 방문할 위치
        next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
        # 다음 방문할 위치가 벽, 범위 밖, 방문했던 곳이 아니어야 한다.
        if board[next_position[0]][next_position[1]] == 1 or next_position in visited_positions:
            continue

        # 현재 방향과 다음 방향이 같다면, 직선으로 나아간다는 것.
        if current_direction == direction:
            # 직선 방향으로 나아갈 경우
            possible_next_positions.append((next_position, direction,
                                            count_of_current_straight_road_or_corner + 1, current_corner, corner_limit))
        else:
            # 현재 방향과 다음 방향이 같지 않다면,
            # 현재 칸에서 90도로 회전한다는 것.
            # 즉, 현재 칸에서 코너가 만들어 진다는 것.
            if current_corner == corner_limit:
                # 이미 최대 가능 코너 갯수를 다 썼다면,
                # 코너를 더이상 만들 수 없다.
                continue
            else:
                # 아직 최대 가능 코너 갯수를 다 쓰지 않았다면,
                # 다음 위치는 현재 위치랑 같다.
                possible_next_positions.append((current_position, direction,
                                                count_of_current_straight_road_or_corner + 1, current_corner + 1, corner_limit))

    return possible_next_positions


def solution(board):
    N = len(board)

    # 계산 쉽게 하기 위해 바깥 부분을 1로 둘러쌈
    # 출발점 (1, 1)
    # 도착점 (N, N)
    board_extension = [[1 for col in range(N + 2)] for row in range(N + 2)]

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                board_extension[row + 1][col + 1] = 0

    board = board_extension

    all_costs = []

    # 존재 가능한 코너의 갯수는 1개 이상 N * N개 이하
    for corner_limit in range(1, N * N + 1):
        visited_positions_queue = Queue()
        # (현재 좌표(x좌표, y좌표), 해당 좌표에서의 경로의 방향, 해당 좌표까지 쓰인 직진도로 또는 코너의 갯수,
        # 해당 좌표까지 쓰인 코너의 갯수, 가능한 총 코너 갯수 제한)
        visited_positions_queue.put(((1, 2), (1, 0), 0, 0, corner_limit))
        visited_positions_queue.put(((2, 1), (0, 1), 0, 0, corner_limit))

        visited_positions = [(1, 1), (1, 2), (2, 1)]

        costs_in_corner_limit = []

        while not visited_positions_queue.empty():
            visited_position = visited_positions_queue.get()
            next_positions = find_next_position(*visited_position, board, visited_positions)
            for next_position in next_positions:
                if next_position[0] == (N, N) and next_position[3] == corner_limit:
                    # 목적지 도착 시, 현재 비용 계산해서 저장
                    count_of_straight_road = next_position[2] - corner_limit
                    count_of_corner = corner_limit
                    print('코너 제한 {}개에서 직진도로 {}개, 코너 {}개로 도착'.format(corner_limit, count_of_straight_road, count_of_corner))
                    current_total_cost = (100 * count_of_straight_road) + (500 * count_of_corner)
                    costs_in_corner_limit.append(current_total_cost)
                    break
                visited_positions.append(next_position[0])
                visited_positions_queue.put(next_position)
        if len(costs_in_corner_limit) > 0:
            all_costs.append(sorted(costs_in_corner_limit)[0])
    return sorted(all_costs)[0]


print(solution([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]))

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
