"""
[ 2020 카카오 인턴십 ] 경주로 건설

출발점부터 도착점까지 경주로를 건설해야 한다.
경주로를 건설한다는 것은,
직선도로 또는 코너들을 설치해 출발점부터 도착점까지 잇는 것이다.

문제에서 경주로를 건설하는데 필요한 최소비용을 구하라고 한다.
이를 위해 최단거리경로 찾기 알고리즘인 BFS를 사용한다.
BFS는 거리순서 1, 2, 3, 4, ... 순으로 탐색하는 알고리즘이다.
그렇게 거리순서대로 탐색하다가, 목적지에 다다르면 바로 탐색을 끝내고 그 순간의 거리를 반환한다.
거리 오름차순 순서대로 탐색하다가 목적지에 다다르자마자 바로 반환한 거리이므로
이는 최단거리의 경로이다.

따라서 BFS로 이를 해결하기 위해 경주로를 건설하는데 드는 총 비용을 거리로 둔다.
그리고 최단거리(여기서는 최소비용)의 경로를 찾으면 된다.

하지만 이 문제에서의 문제점은 경주로 건설에 쓰이는 직선도로와 코너가 각각 비용이 다르다는 것이다.
이 문제에서는 직선도로를 놓을 때는 100원, 코너를 놓을 때는 500원으로,
한 위치의 노드에서 직선도로 설치 또는 코너 설치를 한 자식노드들의 총 비용 증가량이 다르다.
BFS에서는 비용이 A인 노드들, 비용이 A + a인 노드들, 비용이 A + 2a인 노드들... 순으로 탐색되어야 한다.
그래야 어떤 노드가 목적지에 다다르자마자 탐색을 종료하고 해당 노드를 선택했을 때,
그 노드의 비용이 최소비용이 된다.
하지만 이 문제의 경우처럼 자식노드들의 총 비용 증가량이 다르면,
위처럼 비용의 오름차순 순으로 탐색이 안된다.

그럼 BFS의 큐를 정렬하거나, 다익스트라를 쓰면 되지 않느냐? 라고 반문할 수도 있다.
하지만 이들은 대부분의 비정교한 테스트케이스들에서는 무난히 통과가 되겠지만,
엄격하게 이론상으로는 안된다.
A경로가 (a행, b열)에 있다고 해보자.
이 때 A경로가 여태까지 쓴 비용은 COST1 이다.
그리고 A경로는 아래방향을 보고 있었다.
이 A경로가 오른쪽 방향으로 꺾어서 코너를 들고 직진했다.
그래서 DEST(a행, b + 1열)라는 목적지에 도달했다.
코너를 만들면서 돌았기 때문에 A에는 600원(코너 500원 + 직선도로 100원)이 추가된다.
따라서 경로A가 DEST까지 경주로를 건설하는데 든 총 비용은 COST1 + 600원 이다.

그리고 다른 경로 B가 (a행, b - 1열)에서 오른쪽 방향을 보고 있었다.
이 B 경로가 여태까지 쓴 비용은 COST1 + 100원 이다.
경로 B가 직진을 하려고 할 때, 경로 A가 코너를 만들면서 돌아간 (a행, b열)을 갈 수가 없다.
왜냐하면 (a행, b열)에 저장된 가격은 COST1이고, 경로 B가 이곳을 갈 때 드는 비용은 COST1 + 200원으로 더 비싸기 때문이다.

하지만 문제는, 만약 경로B가 이를 무시하고 DEST(a행, b + 1열)에 도달했을 경우 총 비용은 COST1 + 300원 이다.
경로 A는 아까 DEST까지 쓴 총 비용이 COST1 + 600원 이다.
경로 B가 그냥 그대로 직진이 가능했다면, 비용적으로 더 이득을 볼 수 있는데 그러지 못한 상황이다.

BFS의 큐를 정렬하든, 다익스트라를 쓰든 최소비용 선택으로 COST1이 (a행, b열)에 저장되고,
(a행, b - 1열)에서 (a행, b열)으로 진입 자체를 못한다.
따라서 위와같은 예외가 발생한다.
물론, 두칸을 한번에 전진하는 경우도 추가하면 커버될 것 같기도 하다.
하지만 여기서는, 조금 더 깔끔한 다른 방법을 쓰겠다.


사용된 직선도로의 비용 또는 사용된 코너의 비용을 고정시킨다.
여기서는 사용된 코너의 비용을 고정시킨다.
그러면 목적지에 도착하는 경로의 순서는 똑같이 경주로를 건설하는데 든 총 비용이 작은 순이다.
하지만 여기서 고정한 사용된 코너의 비용을 사용한 경로만 선택하면?
예를들어, 사용된 코너의 비용을 CORNER원으로 고정했다고 하자.
목적지에 도착하는 경로의 순서는 경주로를 건설하는데 든 총 비용이 작은 순이다.
여기에서 사용된 코너의 비용이 CORNER원인 경로만 찾는다.
그러면, 총 비용 = CORNER원 + 직선도로 사용비용 의 오름차순으로 나온다.
이 조건으로 제일 처음에 나오는 경로를 선택하면,
사용된 코너의 비용이 CORNER원인 경우들 중, 최소비용이 든 경로이다.

이제 가능한 모든 CORNER원의 경우를 탐색한다.

사용된 코너 비용이 (500원 * 1개)일 때 목적지까지 도착하는 최소비용,
사용된 코너 비용이 (500원 * 2개)일 때 목적지까지 도착하는 최소비용,
사용된 코너 비용이 (500원 * 3개)일 때 목적지까지 도착하는 최소비용,
...
사용된 코너 비용이 (500원 * X개)일 때 목적지까지 도착하는 최소비용,
들을 모두 구한다.

그리고 이 최소비용들 중 최솟값을 구하면
전체 경주로를 건설하는데 드는 최소비용이 된다.

한 칸에 하나의 코너를 설치할 수 있다.
즉, 설치할 수 있는 코너의 수는 1개 ~ 빈 칸의 갯수 이다.
"""

from queue import Queue

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)

START = 'start'
GO_STRAIGHT = 'go_straight'
TURN_LEFT = 'turn_left'
TURN_RIGHT = 'turn_right'


def find_next_direction_when_turn(current_direction, next_task):
    all_directions = [UP, RIGHT, DOWN, LEFT]
    index_of_current_direction = all_directions.index(current_direction)
    if next_task == TURN_LEFT:
        index_of_next_direction = index_of_current_direction - 1
        if index_of_next_direction < 0:
            index_of_next_direction = 3
        return all_directions[index_of_next_direction]

    elif next_task == TURN_RIGHT:
        index_of_next_direction = index_of_current_direction + 1
        if index_of_next_direction > 3:
            index_of_next_direction = 0
        return all_directions[index_of_next_direction]


def find_next_position_informs(position_inform_to_check, visited_positions, board, number_of_corners_for_checking):
    # position_inform_to_check = (현재위치(행, 열), 현재 바라보고 있는 방향, 현재까지 쓰인 직진도로 또는 코너의 갯수, 현재까지 쓰인 코너의 갯수, 현재 수행한 작업)
    current_position, current_direction, current_number_of_structures, current_number_of_corners, current_task = position_inform_to_check
    possible_next_position_informs = []

    # 다음 작업들
    for next_task in [GO_STRAIGHT, TURN_LEFT, TURN_RIGHT]:

        if next_task == GO_STRAIGHT:
            # 직진할 때,
            next_position = (current_position[0] + current_direction[0], current_position[1] + current_direction[1])
            next_direction = current_direction

            if board[next_position[0]][next_position[1]] == 1 or next_position in visited_positions:
                continue

            possible_next_position_informs.append((next_position, next_direction, current_number_of_structures + 1, current_number_of_corners, GO_STRAIGHT))
            visited_positions.append(next_position)

        elif current_task == GO_STRAIGHT and current_number_of_corners < number_of_corners_for_checking:
            # 현재 방향 기준으로 왼쪽으로 회전
            next_position = current_position
            next_direction = find_next_direction_when_turn(current_direction, next_task)

            possible_next_position_informs.append((next_position, next_direction, current_number_of_structures + 1, current_number_of_corners + 1, next_task))

    return possible_next_position_informs


def bfs(start_position_inform, N, number_of_blanks, board, all_costs):

    # 존재 가능한 코너의 갯수는 비어있는 칸의 갯수만큼 이다.
    for number_of_corners_for_checking in range(1, number_of_blanks + 1):
        queue = Queue()
        queue.put(start_position_inform)
        visited_positions = [(1, 1), start_position_inform[0]]

        found_min_number_of_constructor_case = False

        while not queue.empty():
            position_inform_to_check = queue.get()
            next_position_informs = find_next_position_informs(position_inform_to_check, visited_positions, board, number_of_corners_for_checking)
            for next_position_inform in next_position_informs:
                # position_inform_to_check = (현재위치(행, 열), 현재 바라보고 있는 방향, 현재까지 쓰인 직진도로 또는 코너의 갯수, 현재까지 쓰인 코너의 갯수, 현재 수행한 작업)
                if next_position_inform[0] == (N, N) and next_position_inform[3] == number_of_corners_for_checking:
                    # 목적지 도착 시, 해당 정보가 검사하고있던 코너 갯수 조건에서 최소 비용.
                    # 현재 비용 계산해서 저장
                    count_of_straight_road = next_position_inform[2] - next_position_inform[3]
                    count_of_corner = next_position_inform[3]
                    current_total_cost = (100 * count_of_straight_road) + (500 * count_of_corner)
                    all_costs.append(current_total_cost)
                    found_min_number_of_constructor_case = True
                    break
                queue.put(next_position_inform)


def solution(board):

    N = len(board)
    # 빈 칸의 갯수
    number_of_blanks = 0

    """
    계산 쉽게 하기 위해 바깥 부분을 1로 둘러쌈
    출발점 (1, 1) -> 도착점 (N, N)
    """
    board_extension = [[1 for col in range(N + 2)] for row in range(N + 2)]

    for row in range(N):
        for col in range(N):
            if board[row][col] == 0:
                board_extension[row + 1][col + 1] = 0
                number_of_blanks += 1

    board = board_extension
    all_costs = []

    # (현재위치(행, 열), 현재 바라보고 있는 방향, 현재까지 쓰인 직진도로 또는 코너의 갯수, 현재까지 쓰인 코너의 갯수, 현재 수행한 작업)
    start_position_inform = ((0, 0), START, 0, 0, START)
    bfs(start_position_inform, N, number_of_blanks, board, all_costs)

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