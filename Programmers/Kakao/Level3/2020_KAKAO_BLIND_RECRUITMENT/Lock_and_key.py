from copy import deepcopy
"""
자물쇠와 열쇠
"""


def answer_check(extension_lock, lock_size, lock_additional_one_side_size):
    for row in range(lock_additional_one_side_size, (lock_additional_one_side_size + lock_size - 1) + 1):  # index : 2 ~ 4(2 + 3 - 1)
        for col in range(lock_additional_one_side_size, (lock_additional_one_side_size + lock_size - 1) + 1):
            if extension_lock[row][col] != 1:
                return False
    return True


def make_extension_rock(tmp_lock, extension_lock_size, lock_additional_one_side_size, lock_size):
    extension_lock = [[1 for col in range(extension_lock_size)] for row in range(extension_lock_size)]
    for row in range(lock_additional_one_side_size,
                     (lock_additional_one_side_size + lock_size - 1) + 1):  # index : 2 ~ 4(2 + 3 - 1)
        for col in range(lock_additional_one_side_size, (lock_additional_one_side_size + lock_size - 1) + 1):
            extension_lock[row][col] = tmp_lock[row - lock_additional_one_side_size][
                col - lock_additional_one_side_size]
    return extension_lock


def check_case(key, lock):
    tmp_key = deepcopy(key)
    tmp_lock = deepcopy(lock)

    key_size = len(tmp_key)  # 3
    lock_size = len(tmp_lock)  # 3
    lock_additional_one_side_size = key_size - 1  # 2
    extension_lock_size = lock_size + (lock_additional_one_side_size * 2)  # 3 + (2 * 2)

    for extension_lock_try_row in range(extension_lock_size - lock_additional_one_side_size):
        for extension_lock_try_col in range(extension_lock_size - lock_additional_one_side_size):
            extension_lock = make_extension_rock(tmp_lock, extension_lock_size, lock_additional_one_side_size, lock_size)
            for key_row in range(key_size):
                for key_col in range(key_size):
                    extension_lock[extension_lock_try_row + key_row][extension_lock_try_col + key_col] \
                        += key[key_row][key_col]
            if answer_check(extension_lock, lock_size, lock_additional_one_side_size):
                return True
            else:
                continue
    return False


def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret


def solution(key, lock):
    current_key = key
    for _ in range(4):
        if check_case(current_key, lock):
            return True
        else:
            current_key = rotate_90(current_key)
    return False


