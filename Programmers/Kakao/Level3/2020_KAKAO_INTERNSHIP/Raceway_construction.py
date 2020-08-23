from copy import deepcopy
from queue import Queue

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)


def find_next_position_informs(position_inform, board):
    current_position, current_direction, current_cost = position_inform
    # 가능한 다음 작업들 저장할 리스트
    next_position_informs = []
    # 현재 지점에서 나아갈 수 있는 모든 방향 검사
    for next_direction in [LEFT, RIGHT, UP, DOWN]:
        # 해당 방향으로 진행시 다음 위치
        next_position = (current_position[0] + next_direction[0], current_position[1] + next_direction[1])

        # 만약 다음 위치가 벽이거나 범위 밖이면
        if board[next_position[0]][next_position[1]] == 1:
            continue

        # 만약 현재 방향과 반대방향이면
        if next_direction == (-1 * current_direction[0], -1 * current_direction[0]):
            continue

        # 직진, 회전에 따른 다음 위치에서의 비용
        next_cost = current_cost + (100 if current_direction == next_direction else 600)

        # 만약 최소비용을 board상에 저장한 적이 없거나(값이 0일 때),
        # 현재 계산한 다음 위치의 비용이 기존에 저장한 최소비용보다 작으면 채택
        if board[next_position[0]][next_position[1]] == 0 or board[next_position[0]][next_position[1]] > next_cost:
            next_position_informs.append((next_position, next_direction, next_cost))

    # 다음 작업들 반환
    return next_position_informs


def bfs(start_right_direction_position_inform, board, all_costs, N):
    queue = Queue()
    queue.put(start_right_direction_position_inform)
    # 큐 안에 데이터가 존재하는 동안 계속 반복
    # 가장 먼저 도착점에 도착하는 작업의 비용이 최솟값이 아닐 수도 있기 때문.
    while not queue.empty():
        position_inform = queue.get()
        next_position_informs = find_next_position_informs(position_inform, board)
        for next_position_inform in next_position_informs:
            # 가능한 다음 작업들을 하나씩 꺼낸다.
            # 큐에 삽입하고 board에 현재 최소비용 저장
            queue.put(next_position_inform)
            board[next_position_inform[0][0]][next_position_inform[0][1]] = next_position_inform[2]

    # 더이상 갱신할 최소비용이 없는 경우 도착점의 최소비용 최종 최소비용에 추가.
    all_costs.append(board[N][N])


def solution(board):

    N = len(board)

    # 계산 편하게 하기 위해 board 테두리를 1로 둘러싼다.
    # 출발점(1, 1) -> 도착점(N, N)
    board_extension = [[1 for row in range(N + 2)] for col in range(N + 2)]

    # board의 값 테두리 안에 그대로 대입
    for row in range(N):
        for col in range(N):
            board_extension[row + 1][col + 1] = board[row][col]

    """
    각 출발 방향별로 새로운 board 사용한다.
    """
    board1 = deepcopy(board_extension)
    board2 = deepcopy(board_extension)

    # 총 계산결과 저장할 리스트
    all_costs = []

    # (현재 위치(행, 열), 현재 바라보고있는 방향, 현재까지 비용)
    # 오른쪽 방향 시작
    start_right_direction_position_inform = ((1, 1), RIGHT, 0)
    # 아래 방향 시작
    start_down_direction_position_inform = ((1, 1), DOWN, 0)

    # 시작 부분 막는다.
    board[1][1] = 1

    # 오른쪽 방향으로 출발하여 탐색
    bfs(start_right_direction_position_inform, board1, all_costs, N)
    # 아래 방향으로 출발하여 탐색
    bfs(start_down_direction_position_inform, board2, all_costs, N)

    # 두 결과중 최솟값 반환
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
#2100

print(solution([
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0]
]))
# 3200

print(solution([
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 0, 0]
]))
# 3000
