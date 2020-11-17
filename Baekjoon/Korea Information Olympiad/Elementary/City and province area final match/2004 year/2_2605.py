"""
2605번
줄 세우기
"""

N = int(input())

number_chosen_by_student_list = list(map(int, input().split()))

final_student_line_up_order_list = []

student_sequence_number = 1

for chosen_number in number_chosen_by_student_list:

    if chosen_number == 0:
        final_student_line_up_order_list.append(student_sequence_number)
    else:
        final_student_line_up_order_list.insert(
            len(final_student_line_up_order_list) - chosen_number,
            student_sequence_number
        )

    student_sequence_number += 1


for student_number in final_student_line_up_order_list:
    print(student_number, end=' ')
