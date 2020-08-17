from queue import Queue

"""
블록 이동하기
"""

"""
current_position = {(x1, y1), (x2, y2)}
part1 = (x1, y1)
part2 = (x2, y2)
"""


def get_next_positions_to_visit(board_extension, visited_position):
    # visited_position set형태이다.
    # set형태는 순서가 없어서 index로 접근할 수 없다.
    # 따라서, 아래와 같이 list로 변환한 후에 index로 접근해야 한다.
    visited_position = list(visited_position)
    # 로봇을 반으로 쪼개 두 파트로 나눈다.
    part1 = visited_position[0]  # (x1, y1)
    part2 = visited_position[1]  # (x2, y2)
    # 다음 위치로 가능한 경우들을 모두 여기에 담아 마지막에 반환한다.
    next_positions = []

    # 상하좌우 이동
    # 이동시에 각 x좌표와 y좌표에 더해질 값들의 모든 경우이다.
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    # 모든 이동 경우를 하나씩 꺼낸다.
    for move in moves:
        # 이동할 위치가 extension_board상에서 0으로 비어있어야 이동할 수 있다.
        if board_extension[part1[0] + move[0]][part1[1] + move[1]] == 0 \
                and board_extension[part2[0] + move[0]][part2[1] + move[1]] == 0:
            # 이동 가능하면, 이동한 위치를 새로 set형태로 생성하여, next_positions에 추가한다.
            next_positions.append({(part1[0] + move[0], part1[1] + move[1]), (part2[0] + move[0], part2[1] + move[1])})

    # 회전
    rotates = [1, -1]
    # 가로로 놓여있을 때
    # 로봇의 두 부분 (part1과 part2)의 y값이 서로 같으면 로봇이 가로로 놓여있는 것이다.
    if part1[1] == part2[1]:
        # 1 또는 -1을 순서대로 꺼낸다.
        for rotate in rotates:
            # 위 또는 아래 비었는지 검사
            # 로봇이 가로로 놓여있을 때,
            # 로봇의 part1, part2 각각의 윗칸이 모두 0으로 비어있어야 위쪽으로 회전이 가능하다.
            # 어느 한 쪽도 비어있지 않으면 위로 회전 자체가 불가능하다.
            # 아래쪽으로 회전도 같은 원리이다.
            if board_extension[part1[0]][part1[1] + rotate] == 0 \
                    and board_extension[part2[0]][part2[1] + rotate] == 0:
                next_positions.append({(part1[0], part1[1]), (part1[0], part1[1] + rotate)})
                next_positions.append({(part2[0], part2[1]), (part2[0], part2[1] + rotate)})
    else:
        # 세로로 놓여있을 때
        for rotate in rotates:
            # 왼쪽 또는 오른쪽 비었는지 검사
            # 로봇이 세로로 놓여있을 때,
            # 로봇의 part1, part2 각각의 왼쪽칸이 모두 0으로 비어있어야 왼쪽으로 회전이 가능하다.
            # 어느 한 쪽도 비어있지 않으면 왼쪽으로 회전 자체가 불가능하다.
            # 오른쪽으로 회전도 같은 원리이다.
            if board_extension[part1[0] + rotate][part1[1]] == 0 \
                    and board_extension[part2[0] + rotate][part2[1]] == 0:
                next_positions.append({(part1[0] + rotate, part1[1]), (part1[0], part1[1])})
                next_positions.append({(part2[0] + rotate, part2[1]), (part2[0], part2[1])})

    return next_positions


def solution(board):
    # 지도 한 변의 길이
    N = len(board)
    # 외벽을 모두 1로 둘러싸서 연산 쉽게 함
    board_extension = [[1 for _ in range(N + 2)] for _ in range(N + 2)]
    for col in range(N):
        for row in range(N):
            board_extension[row + 1][col + 1] = board[row][col]

    # 시작 시간 0초
    start_time = 0

    # 시작 로봇 위치
    # 집합으로 정의한 이유는, 집합은 순서가 없으므로, 로봇의 왼쪽 오른쪽 두 부분을 구분짓지 않기 위함이다.
    # 만약 두 부분을 구분짓는다면, 로봇이 같은 칸을 차지하더라도, 로봇이 180도 뒤집혀 있는 경우,
    # 2가지의 다른 경우로 보게되어 중복이 된다.
    # 예를 들어,
    # ((1, 1), (1, 2)) (시작점) 에서 반시계 방향으로 90도 회전하면 -> ((2, 2), (1, 2)) 가 된다.
    # 다른 경우로, ((1, 1), (1, 2)) (시작점) 에서
    # 시계방향으로 90도 회전하고 -> ((1, 1), (2, 1))
    # 오른쪽으로 한 칸 이동하면 -> ((1, 2), (2, 2)) 이 된다.
    # 위의 두 경우는 같은 칸을 차지하여 문제상에서 같은 경우이지만,
    # 로봇의 왼쪽 오른쪽을 튜플로 구분지으니 다른 경우로 나타나게 된다.
    # 따라서, 이러한 중복을 막기 위해 집합으로 정의한다.
    start_robot_position = {(1, 1), (1, 2)}
    # BFS 탐색 구현을 위해 방문한 위치와 그 때의 시간을 저장할 큐 생성
    queue_for_bfs = Queue()
    # [방문한 로봇의 위치, 방문 시간]의 리스트를 만들어 큐에 put
    queue_for_bfs.put([start_robot_position, start_time])
    # 이미 방문한 위치를 저장할 list 선언
    visited_positions = []
    # 목적지 (N, N)
    destination = (N, N)

    # BFS 탐색을 위한 큐가 비어있지 않는 한 계속 반복
    while not queue_for_bfs.empty():
        # BFS 탐색을 위한 큐에서 하나를 꺼낸다. (이미 방문한 위치와 시간임.)
        visited_position_and_time = queue_for_bfs.get()

        # 함수에 지도와 방문한 위치를 매개변수로 넘겨, 다음 1초동안 방문할 수 있는 모든 위치의 경우들을 가져온다.
        next_positions_can_visit = get_next_positions_to_visit(board_extension, visited_position_and_time[0])

        # 다음 1초동안 방문할 수 있는 모든 위치의 경우들을 하나씩 차례대로 꺼낸다.
        for next_position in next_positions_can_visit:
            # 방문 가능한 위치가 이미 방문한 위치가 아니라면,
            if next_position not in visited_positions:
                # 방문한다.
                # 만약 현재 방문한 로봇의 위치 중에서 목적지가 포함되어 있으면,
                # 목적지에 도달한 것이므로,
                # 이 방문에 해당하는 방문 시간을 바로 반환한다.
                if destination in next_position:
                    return visited_position_and_time[1] + 1
                # 목적지가 아니라면,
                # BFS 탐색을 위한 Queue에 방문한 위치와 위의 visited_position_and_time에서의 방문 시간 + 1을 넣는다.
                queue_for_bfs.put([next_position, visited_position_and_time[1] + 1])
                # 그리고, 방문한 위치 전체를 저장하는 list에도 추가한다.
                visited_positions.append(next_position)
