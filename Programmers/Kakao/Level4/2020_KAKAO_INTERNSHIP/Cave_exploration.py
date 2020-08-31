"""
동굴 탐험
"""

from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)


# 사이클이 생기는지 검사하는 함수
def is_cycle(after_number, is_visited, after_not_cycle_checked, order_dict):
    # 만약 현재 검사하는 방 번호가 이미 방문한 방 번호라면,
    # 사이클이 발생한 것이므로, 무조건 True를 반환한다.
    if is_visited[after_number]:
        return True

    # 현재 검사하는 방 번호부터 시작되는 검사(현재 방 번호 이하의 방 번호들에 대한 검사)가
    # 사이클이 발생하지 않음이 이미 체크되어있다면
    # 이 이후의 검사는 해봤자 어차피 False(사이클이 발생하지 않음) 이므로
    # False를 반환한다.
    # 만약 현재 방 번호부터 시작되는 검사중에 사이클이 발생했다면 즉시
    # 검사가 중단되고 사이클 발생했음(True)를 반환했을 것이기 때문이다.
    if after_not_cycle_checked[after_number]:
        return False

    # 방문했음을 체크한다.
    is_visited[after_number] = True
    
    # after_number 이전에 방문해야 하는 방 번호(before_number)를 하나씩 꺼낸다.
    for before_number in order_dict[after_number]:
        # before_number가 사이클이 생기는지 검사한다.
        if is_cycle(before_number, is_visited, after_not_cycle_checked, order_dict):
            return True

    """
    방문 역순의 다음 순서가 더이상 없을 때 까지 계속 dfs를 한다.
    여기로 넘어왔으면, 현재 after_number부터 시작했을 때 사이클이 생기지 않음을 의미한다.
    따라서, after_number 이후의 역순 방문은 사이클이 발생하지 않음을 체크한다.
    그리고, 다음 dfs 검사에서 visited 재사용을 위해 False로 다시 바꿔준다.
    사이클이 발생하지 않았음(False)를 반환한다. 
    """
    after_not_cycle_checked[after_number] = True
    is_visited[after_number] = False
    return False


# {이후에 방문해야 하는 방 번호: [이전에 방문해야 하는 방 번호 1, 이전에 방문해야 하는 방 번호 2, ... ]}
# 역방향 방문 순서 dict 만들기
def set_order_dict(before_room_number, current_room_number, order_dict, link_dict):
    # current_room_number 이전에 방문해야 하는 방 번호는 before_room_number이다.

    # link_dict[current_room_number]에 해당하는 값은
    # current_room_number와 연결되어있는 모든 방들의 번호를 원소로 갖는 리스트이다.
    # 이 리스트에서 current_room_number와 연결되어있는 방의 번호를 하나씩 꺼낸다.
    for after_room_number in link_dict[current_room_number]:
        if after_room_number == before_room_number:
            # 만약 연결되어있는 방의 번호가
            # current_room_number 이전에 방문해야 하는 방의 번호(before_room_number) 라면
            # 필요 없으므로 버리고 연결되어있는 다른 방 번호를 꺼낸다.
            continue

        # 여기로 넘어왔으면,
        # after_room_number는 current_room_number 이후에 방문해야 하는 방 번호이다.
        # 이후에 방문해야 하는 방 번호(after_room_number)가 더이상 존재하지 않으면
        # current_room_number는 리프노드(맨 아래 끝 노드)이므로 재귀가 끝나고 return된다.
        # {이후에 방문해야 하는 방 번호: [이전에 방문해야 하는 방 번호 1, 이전에 방문해야 하는 방 번호 2, ... ]}
        # {after_room_number: [..., current_room_number]}
        # 역방향 순서로 저장하는 과정이다.
        order_dict[after_room_number].append(current_room_number)
        # after_room_number를 current_room_number로 하여 재귀호출
        set_order_dict(current_room_number, after_room_number, order_dict, link_dict)


def solution(n, path, order):
    # 연결되어있는 방들의 정보를 저장할 dict
    link_dict = defaultdict(list)
    # 연결되어있는 방들의 방문 순서 정보를 저장할 dict
    # 역방향 순서 정보를 저장
    # {이후에 방문해야 하는 방 번호: [이전에 방문해야 하는 방 번호 1, 이전에 방문해야 하는 방 번호 2, ... ]}
    order_dict = defaultdict(list)

    # 연결 정보이기 때문에, 방향을 양방향으로 저장한다.
    # {A번 방: [A번 방과 연결되어있는 방 1, A번 방과 연결되어있는 방 2]}
    for a, b in path:
        link_dict[a].append(b)
        link_dict[b].append(a)

    # link_dict의 정보로 order_dict 생성
    # 매개변수는 (이전에 방문해야 하는 방 번호, 이후에 방문해야 하는 방 번호, order_dict, link_dict)
    # 0번 방에 유일한 입구가 연결되어 있으므로, 모든 방들은 방문되기 위해서 0번 방을 무조건 거쳐가야 한다.
    # 따라서 0번 방부터 순서를 따져봐야 한다.
    # 여기서 이전에 방문해야 하는 방 번호(-1)은 의미없는 숫자임.
    set_order_dict(-1, 0, order_dict, link_dict)

    # 순서 리스트를 하나씩 꺼낸다.
    for one_order in order:
        """
        순서 리스트는 [이전에 방문해야 하는 방 번호, 이후에 방문해야 하는 방 번호] 이다.
        현재 만들고 있는것은 역방향 순서 정보를 저장하는 dict이므로,
        order_dict[이후에 방문해야 하는 방 번호] = [ ... , 이전에 방문해야 하는 방 번호] 로 추가한다.
        """
        order_dict[one_order[1]].append(one_order[0])

    # 각 방 번호를 index로 하여, 각 방에 대해 방문했는지 체크하는 리스트
    is_visited = [False for _ in range(n)]
    # 각 방 번호를 index로 하여, 각 방에 대해 사이클이 일어나지 않음을 확인했는지 체크하는 리스트
    after_not_cycle_checked = [False for _ in range(n)]
    # 모든 번호의 방을 시작점으로 하여 사이클 여부를 검사한다.
    for room_number in range(n):
        if is_cycle(room_number, is_visited, after_not_cycle_checked, order_dict):
            """
            room_number를 시작점으로 하여 사이클이 발생한다는 것은,
            order_dict가 방문 역방향 순에 대한 정보이기 때문에
            room_number를 방문하기 이전에 room_number를 방문해야 한다는 뜻이 된다.
            이는 말이 안되고, 결국 room_number를 방문할 수 없다는 의미이므로
            모든 방을 방문할 수 없으므로
            무조건 False를 반환한다.
            """
            return False
    """
    모든 방을 시작점으로 했을 때 사이클이 발생하지 않으면
    모든 방을 방문할 수 있으므로 True를 반환한다.
    """
    return True
