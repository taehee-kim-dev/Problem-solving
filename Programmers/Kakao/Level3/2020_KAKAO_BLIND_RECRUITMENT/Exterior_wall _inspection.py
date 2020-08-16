from itertools import permutations
from copy import deepcopy

"""
외벽 점검
"""


def get_all_weak_by_starting_point(n, weak):
    all_weak = []
    """
    [1, 5, 6, 10]
    [5, 6, 10, n + 1]
    [6, 10, n + 1, n + 5]
    [10, n + 1, n + 5, n + 6]
    """
    for _ in range(len(weak)):
        all_weak.append(deepcopy(weak))
        first_weak_position = weak.pop(0)
        weak.append(n + first_weak_position)
    return all_weak


def delete_all_checked_points(weak_case, start_point, end_point):
    return [weak_point for weak_point in weak_case if not (start_point <= weak_point <= end_point)]


def solution(n, weak, dist):
    # 최대 친구의 수가 8명이고, 최소값을 기록해야 하므로, 그보다 1 많은 9로 설정.
    answer = 9
    # 친구들이 검사할 수 있는 순서의 모든 경우의 수 (permutation)
    dist_permutations = list(permutations(dist, len(dist)))
    # 각 모든 점을 시작점으로 했을 때의 모든 경우의 수
    # 각 원소는 원형 구조를 반영한 거리들
    all_weak = get_all_weak_by_starting_point(n, weak)

    # 모든 시작점 경우의 수들 중 하나를 선택
    for weak_case in all_weak:
        # 친구들의 모든 검사 순서 경우의 수들 중 하나를 선택
        for dist_case in dist_permutations:
            # 리스트를 변형하면서 체크해야 하므로 deepcopy
            current_weak_case = deepcopy(weak_case)
            # 검사를 한 친구들 수를 셀 변수
            count_friends = 0
            # 하나의 검사 순서 경우에서 차례대로 한 친구씩 검사 가능 거리를 꺼냄
            for dist_of_one_friend in dist_case:
                # 일단 이 친구가 검사를 할 것이므로 검사를 한 친구의 수 1 증가
                count_friends += 1
                # 이 친구가 검사를 시작할 위치(가장 앞에 있는 취약점)을 얻음
                start_point = current_weak_case[0]
                # 이 친구가 검사 가능한 거리를 더하여 검사할 수 있는 맨 끝 위치를 얻음
                end_point = start_point + dist_of_one_friend
                # 이 친구가 검사한 취약점을 모두 제거하여 반영
                current_weak_case = delete_all_checked_points(current_weak_case, start_point, end_point)
                if len(current_weak_case) == 0:
                    # 이 친구가 검사를 끝냈을 때, 남아있는 취약점이 없다면, 모든 취약점을 검사한 것임.
                    if count_friends < answer:
                        # 그리고 현재 기록된 최소 검사인원(answer)보다 작다면, 현재까지 최소인원이므로 현재 값으로 변경
                        answer = count_friends
                    # 남은 취약점이 없으면 더이상 검사할 필요가 없으므로 break로 빠져나감
                    break

    # 모든 시작점 경우의 수와 친구들의 검사 순서 경우의 수를 따져봤는데,
    # answer의 값이 9이면, 최대 친구의 수는 8명이므로 8명을 모두 동원했음에도 모든 취약점을 검사하지 못했다는 뜻이다.
    # 따라서 이 경우, 문제에서 제시한 대로 -1을 반환한다.
    if answer == 9:
        answer = -1
    # 아닌 경우, answer값을 반환한다.
    return answer
