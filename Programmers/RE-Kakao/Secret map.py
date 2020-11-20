"""
2018 KAKAO BLIND RECRUITMENT
[1차] 비밀지도
"""


def solution(n, arr1, arr2):
    answer = []
    decrypted_arr1 = []
    decrypted_arr2 = []
    for num1, num2 in zip(arr1, arr2):
        decrypted_arr1.append(list('{0:b}'.format(num1).zfill(n)))
        decrypted_arr2.append(list('{0:b}'.format(num2).zfill(n)))

    for row_i in range(0, n):
        tmp = []
        for col_i in range(0, n):
            if decrypted_arr1[row_i][col_i] == '1' \
                    or decrypted_arr2[row_i][col_i] == '1':
                tmp.append('#')
            else:
                tmp.append(' ')
        answer.append(tmp)

    for row_i in range(0, n):
        answer[row_i] = ''.join(answer[row_i])

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
