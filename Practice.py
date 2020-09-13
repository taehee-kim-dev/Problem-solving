"""
Programmers Kakao Level1까지 완료.

"""

from collections import defaultdict

def solution(v):
    answer = []

    x_point_dict = defaultdict(int)
    y_point_dict = defaultdict(int)

    for x, y in v:
        x_point_dict[x] += 1
        y_point_dict[y] += 1

    for x, count in x_point_dict.items():
        if count == 1:
            answer.append(x)

    for y, count in y_point_dict.items():
        if count == 1:
            answer.append(y)

    return answer


print(solution([[1, 4], [3, 4], [3, 10]]))
