"""
무지의 먹방 라이브
"""


# 음식 객체
class Food:
    def __init__(self, food_number, food_time):
        # 음식 번호
        self.food_number = food_number
        # 이 음식을 먹는 데에 드는 총 시간
        self.food_time = food_time


def solution(food_times, k):
    """
    k초 동안 k번째 음식까지 먹는다.
    k번 째 음식까지 먹고 네트워크 장애가 발생했으므로,
    네트워크 정상화 후 다시 먹기 시작해야할 음식은 k + 1 번째 음식이다.
    """

    # 음식객체들을 담을 리스트
    foods = []

    # 음식번호와 음식시간으로 객체를 만들어서 리스트에 저장
    for food_number, food_time in enumerate(food_times, 1):
        foods.append(Food(food_number, food_time))

    # 처음에 존재하던 전체 음식의 개수
    N = len(food_times)
    # 음식 객체 리스트를 음식시간을 기준으로 오름차순으로 정렬
    foods.sort(key=lambda x: x.food_time)

    # k초까지 음식을 먹는것을 시뮬레이션한다.
    remaining_time = k
    # 직전에 다 먹은 음식의 음식시간
    before_food_time = 0
    for idx, food in enumerate(foods):
        # 현재 먹는 음식의 시간과 직전에 다 먹은 음식의 시간의 차이
        food_time_diff = food.food_time - before_food_time
        # 음식 시간 차이가 0이면 다음으로 넘어간다.
        if food_time_diff == 0:
            continue
        # 남아있는 음식의 수
        number_of_remaining_foods = N - idx
        # 현재 차례에 해당하는 음식을 다 먹는 만큼을
        # 한 번에 전체 음식에서 뺀다.
        time_to_delete = food_time_diff * number_of_remaining_foods
        # 한 번에 지울 시간이 남아있는 시간보다 크면
        # 한 번에 지울 수 없다.
        if time_to_delete > remaining_time:
            # 남아있는 음식들을 따로 리스트로 빼낸다.
            remaining_foods = foods[idx:]
            # 남아있는 음식 객체들을 음식번호 순서대로(원래 순서대로) 다시 정렬한다.
            remaining_foods.sort(key=lambda x: x.food_number)
            # 남아있는 시간을 남아있는 음식의 수로 나누면,
            # 다음 차례에 먹어야 하는 음식의 인덱스가 나온다.
            # 그 인덱스에 해당하는 음식객체의 음식번호를 반환하면 된다.
            return remaining_foods[remaining_time % number_of_remaining_foods].food_number

        # 다음 차례로 넘어갈 때,
        # 한 번에 삭제한 만큼 남아있는 시간을 빼준다.
        remaining_time -= time_to_delete
        # 직전에 다 먹은 음식의 시간을 저장한다.
        before_food_time = food.food_time

    # 이곳까지 왔다면, k초까지 모든 음식을 다 먹었다는 뜻이므로, -1을 반환한다.
    return -1


print(solution([3, 1, 2], 5))
print(solution([3, 5, 1, 6, 5, 3], 20))
