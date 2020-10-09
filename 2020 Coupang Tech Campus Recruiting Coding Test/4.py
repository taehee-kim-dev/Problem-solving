

class Node:
    def __init__(self, city_name):
        self.city_name = city_name
        self.is_departure = False
        self.is_hub = False
        self.is_destination = False
        self.next_nodes = dict()

IS_ROUTE_CONTAIN_HUB = False
def find_route(from_node, to_node):
    pass


def solution(depar, hub, dest, roads):
    answer = 0

    city_nodes = dict()

    city_names = set()
    for from_city_name, to_city_name in roads:
        city_names |= {from_city_name, to_city_name}

    city_names = list(city_names)
    for city_name in city_names:
        city_node = Node(city_name)
        if city_name == depar:
            city_node.is_departure = True
        if city_name == hub:
            city_node.hub = True
        if city_name == dest:
            city_node.is_destination = True
        city_nodes[city_name] = city_node

    for from_city_name, to_city_name in roads:
        pass

    return answer


print(solution("SEOUL",	"DAEGU", "YEOSU", [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]))
# 9

print(solution("ULSAN", "SEOUL", "BUSAN", [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]))
# 0