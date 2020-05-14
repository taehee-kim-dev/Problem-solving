'''
    영상의 가로, 세로를 반으로 쪼갠다.
    즉, 4등분을 한다. 한 점 단위까지 등분을 반복한다.

    등분된 각 부분에 대해서, 압축(병합)을 시도한다.

    각 압축결과가 0이나 1로 모두 동일하면, 등분 전의 부분에 대한 압축 결과는 해당 압축결과 값이다.

    모두 동일하지 않다면,
    '(왼쪽 위 압축 결과, 오른쪽 위 압축 결과, 왼쪽 아래 압축 결과, 오른쪽 아래 압축 결과)'가
    등분 전 부분에 대한 압축 결과가 된다.
'''

N = int(input())

input_video = []

for _ in range(N):
    line = input()
    input_video.append(line)


def solution(size, col_start_index, col_end_index, row_start_index, row_end_index):
    global input_video

    # 가장 작은 단위면 해당 값 반환
    if size == 1:
        return input_video[row_start_index][col_start_index]

    col_half_left_end_index = int((col_start_index + col_end_index - 1) / 2)
    col_half_right_start_index = col_half_left_end_index + 1

    row_half_up_end_index = int((row_start_index + row_end_index - 1) / 2)
    row_half_down_start_index = row_half_up_end_index + 1

    # 왼쪽 위 압축 결과
    left_up_compressed_result = solution(size / 2,
                                         col_start_index, col_half_left_end_index,
                                         row_start_index, row_half_up_end_index)
    # 오른쪽 위 압축 결과
    right_up_compressed_result = solution(size / 2,
                                          col_half_right_start_index, col_end_index,
                                          row_start_index, row_half_up_end_index)
    # 왼쪽 아래 압축 결과
    left_down_compressed_result = solution(size / 2,
                                           col_start_index, col_half_left_end_index,
                                           row_half_down_start_index, row_end_index)
    # 오른쪽 아래 압축 결과
    right_down_compressed_result = solution(size / 2,
                                            col_half_right_start_index, col_end_index,
                                            row_half_down_start_index, row_end_index)

    # 네 결과값이 모두 1 또는 0으로 같을 때
    if (left_up_compressed_result == right_up_compressed_result \
        and left_down_compressed_result == right_down_compressed_result \
        and left_up_compressed_result == left_down_compressed_result) \
            and (left_up_compressed_result == '0' or left_up_compressed_result == '1'):
        # 해당 값 그대로 반환
        return left_up_compressed_result
    else:
        # 그렇지 않을 때,
        # '(왼쪽 위 압축 결과, 오른쪽 위 압축 결과, 왼쪽 아래 압축 결과, 오른쪽 아래 압축 결과)' 형태로 반환
        compressed_result = '(' + \
                            left_up_compressed_result + \
                            right_up_compressed_result + \
                            left_down_compressed_result + \
                            right_down_compressed_result + \
                            ')'

        return compressed_result


print(solution(N, 0, N-1, 0, N-1))
