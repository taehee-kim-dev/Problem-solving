"""
호텔 방 배정
"""


# 호텔 방 노드
class HotelRoom:
    def __init__(self, room_number, next_room_number_to_start_search):
        # 방 번호
        self.room_number = room_number
        # 이 방을 체크했을 때, 다음으로 체크해야 할 방 번호
        self.next_room_number_to_start_search = next_room_number_to_start_search

        # 다음으로 체크해야 할 방 번호 설정 함수
    def set_next_room_number_to_start_search(self, next_room_number_to_start_search):
        self.next_room_number_to_start_search = next_room_number_to_start_search


def solution(k, room_number):
    # 배정된 방 번호들
    assigned_room_numbers = []

    # 이미 배정된 방들을 {방 번호 : 방 노드 객체} 형태로 저장
    already_assigned_room_numbers = dict()

    # 고객들이 원하는 방 번호를 순서대로 하나씩 꺼냄
    for number in room_number:
        # 배정 가능한 방을 체크할 때, 체크한 이미 배정된 방들
        checked_rooms = []
        # 현재 배정 가능 유무를 체크하고있는 방의 번호
        current_checking_room_number = number

        while True:
            if current_checking_room_number not in already_assigned_room_numbers:
                # 만약 현재 체크하고있는 번호의 방이 배정 가능하다면
                break

            # 만약 현재 체크하고있는 번호의 방이 이미 배정되어있는 방이라면
            current_checked_room = already_assigned_room_numbers[current_checking_room_number]
            # 체크한 이미 배정된 방들 리스트에 저장
            checked_rooms.append(current_checked_room)
            # 다음에 체크할 방의 번호를 방금 체크한 방에 저장되어있는 다음 탐색시작 방 번호로 교체
            current_checking_room_number = current_checked_room.next_room_number_to_start_search

        # 현재 체크한 번호의 방이 배정 가능하다면
        # 해당 번호로 방 객체를 만든다.
        # 다음 탐색시작 방 번호는 현재 만든 방 번호 + 1
        new_hotel_room_node_to_be_assigned = HotelRoom(current_checking_room_number,
                                                       current_checking_room_number + 1)
        # 이미 배정된 방 dictionary에 추가
        already_assigned_room_numbers[current_checking_room_number] = new_hotel_room_node_to_be_assigned
        # 배정된 방 번호들 리스트(답)에 방 번호 추가
        assigned_room_numbers.append(current_checking_room_number)

        # 배정 가능한 방을 찾을 때 까지 체크한 모든 방들의 다음 탐색시작 방 번호 또한
        # 방금 배정한 방 번호 + 1로 교체
        for room in checked_rooms:
            room.set_next_room_number_to_start_search(current_checking_room_number + 1)

    return assigned_room_numbers
