from itertools import combinations



def solution(orders, course):
    answer = []

    orders_dict = dict()

    for number_of_menus_in_course in course:
        all_case_of_menus = []
        for menus_of_one_order in orders:
            if len(menus_of_one_order) >= number_of_menus_in_course:
                menu_case = list(combinations(menus_of_one_order, number_of_menus_in_course))
                for one_menu_case in menu_case:
                    all_case_of_menus.append(set(one_menu_case))

        for menu in all_case_of_menus:
            if all_case_of_menus.count(menu) >= 2:
                menu_list = list(menu)
                menu_list.sort()
                menu_str = ''
                for m in menu_list:
                    menu_str += m

                if menu_str not in orders_dict:
                    orders_dict[menu_str] = all_case_of_menus.count(menu)

    for number_of_menus_in_course in course:
        current_length_menus = []
        for menu, length in orders_dict.items():
            if len(menu) == number_of_menus_in_course:
                current_length_menus.append([menu, length])

        if len(current_length_menus) > 0:
            current_length_menus.sort(key=lambda x: x[1])
            max_length = current_length_menus[-1][-1]
            answer.extend([x[0] for x in current_length_menus if x[-1] == max_length])

    answer.sort()

    return answer



print(solution(
    ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]
))
# ["AC", "ACDE", "BCFG", "CDE"]

print(solution(
    ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]
))

print(solution(
    ["XYZ", "XWY", "WXA"], [2, 3, 4]
))
