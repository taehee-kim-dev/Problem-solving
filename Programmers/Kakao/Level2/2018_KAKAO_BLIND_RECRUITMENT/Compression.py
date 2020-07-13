# [3차]압축

dictionary = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def solution(msg):
    answer = []

    checking_last_index = 0
    while True:
        str_to_check = msg[:checking_last_index + 1]
        if str_to_check in dictionary:
            if checking_last_index == len(msg) - 1:
                answer.append(dictionary.index(str_to_check))
                break
        else:
            answer.append(dictionary.index(str_to_check[:-1]))
            dictionary.append(str_to_check)
            msg = msg[checking_last_index:]
            checking_last_index = 0
            continue
        checking_last_index += 1

    return answer
