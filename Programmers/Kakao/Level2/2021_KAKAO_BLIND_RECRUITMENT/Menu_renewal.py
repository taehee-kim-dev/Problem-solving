from itertools import combinations
from collections import defaultdict


def solution(orders, courses_menus_counts):
    answer = []

    for course_menu_count in courses_menus_counts:
        menu_order_counts = defaultdict(int)
        for order in orders:
            order_combinations = list(combinations(order, course_menu_count))
            for order_combination in order_combinations:
                order_combination = ''.join(sorted(order_combination))
                menu_order_counts[order_combination] += 1
        count_matched_courses = {}
        for course, count in menu_order_counts.items():
            if len(course) == course_menu_count:
                count_matched_courses[course] = count
        if len(count_matched_courses) == 0:
            continue
        max_count = max(count_matched_courses.values())
        if max_count < 2:
            continue
        max_count_courses = []
        for count_matched_course, count in count_matched_courses.items():
            if count == max_count:
                max_count_courses.append(count_matched_course)
        answer += max_count_courses

    return sorted(answer)


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
