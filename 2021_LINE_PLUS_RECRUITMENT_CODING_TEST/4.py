import sys
sys.setrecursionlimit(10*8)


UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)


def find_next_left(direction, position):
    if direction == LEFT:
        return [(position[0] + DOWN[0], position[1] + DOWN[1]), DOWN]
    elif direction == RIGHT:
        return [(position[0] + UP[0], position[1] + UP[1]), UP]
    elif direction == UP:
        return [(position[0] + LEFT[0], position[1] + LEFT[1]), LEFT]
    else:
        return [(position[0] + RIGHT[0], position[1] + RIGHT[1]), RIGHT]


def find_next_right(direction, position):
    if direction == LEFT:
        return [(position[0] + UP[0], position[1] + UP[1]), UP]
    elif direction == RIGHT:
        return [(position[0] + DOWN[0], position[1] + DOWN[1]), DOWN]
    elif direction == UP:
        return [(position[0] + RIGHT[0], position[1] + RIGHT[1]), RIGHT]
    else:
        return [(position[0] + LEFT[0], position[1] + LEFT[1]), LEFT]


found = False
total_sec = 0


def find_next_back(direction):
    if direction == LEFT:
        return RIGHT
    elif direction == RIGHT:
        return LEFT
    elif direction == UP:
        return DOWN
    else:
        return UP


def find_way(direction, second, position, N, maze):
    global found, total_sec
    if position == (N - 1, N - 1):
        found = True
        total_sec = second
        return
    next_left = find_next_left(direction, position)
    next_straight = [(position[0] + direction[0], position[1] + direction[1]), direction]
    next_right = find_next_right(direction, position)
    next_back = [(position[0] - direction[0], position[1] - direction[1]), find_next_back(direction)]

    for next_position in [next_left, next_straight, next_right, next_back]:
        if 0 <= next_position[0][0] <= N - 1 and 0 <= next_position[0][1] <= N - 1 \
                and maze[next_position[0][0]][next_position[0][1]] == 0:
            if found:
                return
            find_way(next_position[1], second + 1, next_position[0], N, maze)


def solution(maze):
    answer = 0

    if maze[0][1] == 0:
        # 방향, 초, 현재위치
        find_way(RIGHT, 0, (0, 0), len(maze), maze)
    else:
        find_way(DOWN, 0, (0, 0), len(maze), maze)

    return total_sec



print(solution(
[
    [0, 1, 0, 1],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [1, 0, 1, 0]
]
))
# 10

print(solution(
[[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]
))
# 32

print(solution(
[[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]
))
# 24

print(solution(
[[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]
))
# 22
