# [3차] 파일명 정렬


all_files = []


def solution(files):
    answer = []

    for one_file in files:
        origin_file_name = one_file
        file_head = ''
        file_number = ''

        checking_index = 0
        while checking_index <= len(one_file) - 1 \
                and not one_file[checking_index].isdigit():
            file_head += one_file[checking_index]
            checking_index += 1
        number_length_check = 0
        while checking_index <= len(one_file) - 1 \
                and number_length_check <= 5 \
                and one_file[checking_index].isdigit():
            file_number += one_file[checking_index]
            checking_index += 1
            number_length_check += 1

        all_files.append([file_head, int(file_number), origin_file_name])

    sorted_files = sorted(all_files, key=lambda x: (x[0].lower(), x[1]))
    answer = [file[2] for file in sorted_files]

    return answer
