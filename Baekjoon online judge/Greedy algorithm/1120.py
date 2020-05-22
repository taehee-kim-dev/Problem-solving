"""
문자열

두 문자열의 차이 = 동일한 인덱스의 문자가 몇개가 다른가?

문자열 A, 문자열 B
len(A) <= len(B)

A와 B의 길이가 같아질 때 까지
A의 앞 또는 뒤에 아무 알파벳이나 추가할 수 있다.

A와 B의 길이가 같아졌을 때, A와 B의 차이가 최소가 되어야 한다.
"""


def get_min_diff_count():
    all_diff_count = []

    len_diff = len(B) - len(A)

    for B_starting_index in range(len_diff + 1):
        current_diff_count = 0
        for A_index in range(len(A)):
            if A[A_index] != B[B_starting_index + A_index]:
                current_diff_count += 1
        all_diff_count.append(current_diff_count)

    return min(all_diff_count)


# 1 <= len(A), len(B) <= 50
# 소문자로만
A, B = input().split(' ')

print(get_min_diff_count())
