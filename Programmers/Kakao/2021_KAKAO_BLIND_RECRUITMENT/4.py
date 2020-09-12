from collections import defaultdict


def get_fares(start_point_number, fare_board, distances, routes_dict):
    queue = [(start_point_number, 0)]

    while len(queue) > 0:
        current_inform = queue.pop(0)
        current_spot_number = current_inform[0]
        current_fare = current_inform[1]

        for next_spot_number in routes_dict[current_spot_number]:
            if next_spot_number != start_point_number and \
                    (distances[start_point_number][next_spot_number] == 0
                            or distances[start_point_number][next_spot_number] > current_fare + fare_board[current_spot_number][next_spot_number]):
                queue.append((next_spot_number, current_fare + fare_board[current_spot_number][next_spot_number]))
                distances[start_point_number][next_spot_number] = current_fare + fare_board[current_spot_number][next_spot_number]


def solution(n, s, a, b, fares):
    answer = 0

    all_fares = []

    fare_board = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    distances = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    routes_dict = defaultdict(list)

    for fare in fares:
        fare_board[fare[0]][fare[1]] = fare[2]
        fare_board[fare[1]][fare[0]] = fare[2]

        routes_dict[fare[0]].append(fare[1])
        routes_dict[fare[1]].append(fare[0])

    for start_point_number in range(1, n + 1):
        get_fares(start_point_number, fare_board, distances, routes_dict)

    for split_taxi_spot_number in range(1, n + 1):
        # 시작점부터 택시 찢어지는 지점까지 가는 비용
        together_taxi_fare = distances[s][split_taxi_spot_number]
        # 택시 찢어진 지점부터 A의 집까지 가는 비용
        from_taxi_drop_to_A = distances[split_taxi_spot_number][a]
        # 택시 찢어진 지점부터 B의 집까지 가는 비용
        from_taxi_drop_to_B = distances[split_taxi_spot_number][b]
        total_fare = together_taxi_fare + from_taxi_drop_to_A + from_taxi_drop_to_B
        if total_fare > 0:
            all_fares.append(total_fare)

    return min(all_fares)


print(solution(
    6, 4, 6, 2,
    [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
))
# 82

print(solution(
    7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
))
# 14

print(solution(
    6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]
))
# 18
