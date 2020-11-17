"""
백준 11052 카드 구매하기

카드 1개가 포함된 카드팩, 카드 2개가 포함된 카드팩, ... 카드 N개가 포함된 카드팩과 같이 총 N 가지가 존재
i = 카드팩에 있는 카드의 개수
Pi = i개의 카드가 들어있는 카드팩의 가격
N개의 카드를 구매하기 위해 지불해야 하는 금액의 최댓값은?
"""


# (1 ≤ N ≤ 1,000)
N = int(input())


'''
index = 카드팩에 있는 카드의 개수
Pi_list[index] = index 개의 카드가 들어있는 카드팩의 가격 
총 N개의 카드를 구매하되, 전체 지불 가격을 최대로.
index 0은 제외
'''
Pi_list = [-1]

Pi_list.extend(list(map(int, input().split(' '))))


'''
index : 구매한 총 카드 개수
max_price_list_of_card_size[index] : 총 index 개의 카드를 구매할 때의 최대 지불가격
'''
max_price_list_of_card_size = [0]


def solution():
    # 총 N개의 카드를 사야한다.
    """
    동적 계획법 적용
    
    총 current_card_size_to_buy 개의 카드를 사는 경우
    card_size_of_card_pack = 살 수 있는 카드팩에 들어있는 카드의 개수
    1 <= card_size_of_card_pack <= current_card_size_to_buy

    = card_size_of_card_pack 개의 카드가 들어있는 카드팩 구매
        + (current_card_size_to_buy - card_size_of_card_pack)개의 카드 구매
    = Pi_list[card_size_of_card_pack] 
        + max_price_list_of_card_size[current_card_size_to_buy - card_size_of_card_pack]
    """
    # 따라서 총 1개를 사는 경우 부터 N개를 사는 경우까지 차례대로 계산
    for current_card_size_to_buy in range(1, N + 1):
        # 카드팩을 1개짜리부터 총 사려는 개수 짜리까지 살 수 있다.

        # 가능한 가격들을 모두 담을 list
        possible_price_list = []
        for card_size_of_card_pack in range(1, current_card_size_to_buy + 1):
            '''
            현재 총 current_card_size_to_buy 개의 카드를 사야 하는데,
            card_size_of_card_pack 개의 카드가 들어있는 카드팩 하나를 샀으므로,
            
            (current_card_size_to_buy - card_size_of_card_pack) 개를 샀을 때의 최대가격 + 현재 산 카드팩의 가격
            
            의 값들 중 최대값을 구해야 한다.
            '''
            possible_price_list.append(
                max_price_list_of_card_size[current_card_size_to_buy - card_size_of_card_pack]
                + Pi_list[card_size_of_card_pack]
            )

        # max_price_list_of_card_size 의 값들 중 최대값이 현재 사려는 카드 개수를 살 때의 최대 지불 금액이다.
        max_price_list_of_card_size.append(max(possible_price_list))

    return max_price_list_of_card_size[N]


print(solution())
