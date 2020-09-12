from collections import defaultdict




class Person:
    def __init__(self):
        self.number = 0
        self.sale = 0
        self.child_nodes = []


class Tree:
    def __init__(self):
        self.root_node = None


def solution(sales, links):
    answer = 0
    persons_dict = dict()
    links.sort(key=lambda x: x[0])
    link_dict = defaultdict(list)

    for number, sale in enumerate(sales, 1):
        person = Person()
        person.number = number
        person.sale = sale
        persons_dict[number] = person

    for team_boss_number, team_member_number in links:
        link_dict[team_boss_number].append(team_member_number)

    tree = Tree()
    tree.root_node = persons_dict[1]
    for team_boss_number, team_member_numbers_list in link_dict.items():
        boss = persons_dict[team_boss_number]
        for team_member_number in team_member_numbers_list:
            boss.child_nodes.append(persons_dict[team_member_number])




    return answer






print(solution(
    [14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
))
# 44
