from collections import defaultdict


def solution(boxes):
    answer = 0


    number_of_boxes = len(boxes)

    product_dict = defaultdict(int)

    for a, b in boxes:
        product_dict[a] += 1
        product_dict[b] += 1

    number_of_handled_boxes = 0

    for product_number, product_count in product_dict.items():
        if product_count >= 2:
            box_n = product_count // 2
            number_of_handled_boxes += box_n
            product_dict[product_number] = product_count % box_n

    sorted_product_dict = sorted(product_dict.items(), key=lambda x: -x[1])

    if number_of_boxes - number_of_handled_boxes > 0:
        remaining_boxes = number_of_boxes - number_of_handled_boxes
        count = 0
        for product_number, product_count in sorted_product_dict:
            answer += (2 - product_count)
            count += 1
            if count == remaining_boxes:
                break





    return answer







print(solution(
[[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]
))
#

print(solution(
[[1, 2], [3, 4], [5, 6]]
))
#

print(solution(
[[1, 2], [2, 3], [3, 1]]
))
#

