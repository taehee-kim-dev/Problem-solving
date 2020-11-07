"""
이기면 걸었던 액수만큼 돈을 딸 수 있고, 지면 걸었던 액수만큼 돈을 잃습니다.
지면 잃은 돈의 두 배를 다음 판에 베팅합니다.
연속해서 지는 도중에 한 번이라도 이긴다면 다시 기본 금액인 100원을 베팅합니다.
이전 판의 "2배"를 걸어야 하는 상황 = 지는 경우 에서 수중의 돈이 모자라는 경우에는 남은 돈 전부를 건다고 가정합니다.
모든 돈을 잃게 될 경우에는 즉시 게임을 중단하고 더 이상 남은 게임을 진행하지 않습니다.
게임이 끝나고 남은 금액
"""


def solution(money, expected, actual):

    cur_my_betting_money = 100

    for cur_my_expected, cur_actual_result in zip(expected, actual):
        if cur_my_expected == cur_actual_result:
            # 이기면 걸었던 액수만큼 돈을 딸 수 있다.
            money += cur_my_betting_money
            # 이기면 배팅 금액은 다시 100원
            cur_my_betting_money = 100
        else:
            # 지면 걸었던 액수만큼 돈을 일단 잃는다.
            money -= cur_my_betting_money

            # 모든 돈을 잃게 될 경우에는 즉시 게임을 중단하고 더 이상 남은 게임을 진행하지 않습니다.
            if money == 0:
                break
            # 졌을 때, 잃은 돈의 두 배를 걸어야 하는데,
            # 잃은 돈의 두배보다 현재 돈이 적으면, 남은 돈 전부를 건다.
            if money < cur_my_betting_money * 2:
                cur_my_betting_money = money
            else:
                # 그게 아니라면, 잃은 돈의 두 배를 다음 판에 베팅한다.
                cur_my_betting_money *= 2

    return money
