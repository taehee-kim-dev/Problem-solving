from functools import cmp_to_key


def compare(first_num_str, second_num_str):

    first_sum = int(first_num_str + second_num_str)
    second_sum = int(second_num_str + first_num_str)

    return second_sum - first_sum


def solution(numbers):

    number_str_list = list(map(str, numbers))
    sorted_number_str_list = sorted(number_str_list, key=cmp_to_key(compare))

    return str(int(''.join(sorted_number_str_list)))
