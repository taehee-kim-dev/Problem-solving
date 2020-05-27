"""
2309
일곱 난쟁이
"""

N = 9

input_height_list = []
input_height_sum = 0

for _ in range(N):
    input_height = int(input())
    input_height_list.append(input_height)
    input_height_sum += input_height

extra_height_sum = input_height_sum - 100

is_finished = False

for first_height_index in range(len(input_height_list)):
    for second_height_index in range(first_height_index + 1, len(input_height_list)):

        if input_height_list[first_height_index] \
                + input_height_list[second_height_index] == extra_height_sum:

            first_value = input_height_list[first_height_index]
            second_value = input_height_list[second_height_index]

            input_height_list.remove(first_value)
            input_height_list.remove(second_value)

            is_finished = True
            break

    if is_finished:
        break

input_height_list.sort()

for height in input_height_list:
    print(height)
