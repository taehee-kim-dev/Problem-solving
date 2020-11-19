

def convert_to_3_base_num(num: int) -> str:
    result = ''
    m = num
    while m >= 3:
        result = str(m % 3) + result
        m = m // 3
    return str(m) + result


def convert_to_10_base_num(num_str: str) -> int:
    result = 0
    for i in range(0, len(num_str)):
        result += (int(num_str[len(num_str) - 1 - i]) * (3 ** i))
    return result


def solution(n):
    return convert_to_10_base_num(convert_to_3_base_num(n)[::-1])
