"""
[3차] n진수 게임
"""


def convert(n, number):
    result = ''
    while True:
        bottom = int(number / n)
        right = int(number % n)
        if right >= 10:
            right = chr(right - 10 + 65)
        result = str(right) + result
        if bottom == 0:
            break
        number = bottom
    return result


"""
튜브의 순서
p번째 -> p + m 번째 -> (p + m) + m 번째
"""


def solution(n, t, m, p):
    answer = ''
    n_number_str = ''
    n_number_str_len_to_get = p + (m * (t - 1))
    current_number = 0

    while len(n_number_str) < n_number_str_len_to_get:
        n_number_str += convert(n, current_number)
        current_number += 1

    for time in range(t):
        index = p + (m * time) - 1
        answer += n_number_str[index]

    return answer
