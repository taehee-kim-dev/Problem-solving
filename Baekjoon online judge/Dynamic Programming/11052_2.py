"""
백준 11052 카드 구매하기

카드 1개가 포함된 카드팩, 카드 2개가 포함된 카드팩, ... 카드 N개가 포함된 카드팩과 같이 총 N 가지가 존재
i = 카드팩에 있는 카드의 개수
Pi = 카드팩 가격
N개의 카드를 구매하기 위해 민규가 지불해야 하는 금액의 최댓값은?
"""

# (1 ≤ N ≤ 1,000)
N = int(input())

# index 0은 제외
Pi_list = [-1]

Pi_list.extend(list(map(int, input().split(' '))))

'''
index = 카드팩에 있는 카드의 개수
Pi_list[index] = index 개의 카드가 들어있는 카드팩의 가격 
총 N개의 카드를 구매하되, 전체 지불 가격을 최대로.
'''


'''
index : 구매한 총 카드 개수
max_price_list_of_card_size[index] : 총 index 개의 카드를 구매할 때의 최대 지불가격
'''

# 총 1개의 카드를 구매할 때 최대 지불 금액은 1개가 들어있는 카드팩의 가격
max_price_list_of_card_size = [0, Pi_list[1]]


def solution():
    # 총 N개의 카드를 사야한다.
    # 동적 계획법은 이전 단계의 값들이 필요하다.

    # 총 1개의 카드를 구매할 경우는 위에서 미리 넣어놓았으므로,
    # 총 2개의 카드를 사는 경우 부터 N개의 카드를 사는 경우까지 차례대로 계산
    for current_card_size_to_buy in range(2, N + 1):

        # 가능한 가격들을 모두 담을 list
        possible_price_list = []

        '''
        
        기존에 구해서 저장해놓은 총 구매 카드 개수별 최대 가격들의 조합으로 
        current_card_size_to_buy 개의 카드를 살 경우의 가격들을 구할 수 있다.
        
        총 카드 1개를 살 경우의 최대 가격 + 총 카드 current_card_size_to_buy - 1 개를 살 경우의 최대 가격
        총 카드 2개를 살 경우의 최대 가격 + 총 카드 current_card_size_to_buy - 2 개를 살 경우의 최대 가격
        ... 반복 ...
        총 카드 X개를 살 경우의 최대 가격 + 총 카드 current_card_size_to_buy - X 개를 살 경우의 최대 가격
        
        여기에 current_card_size_to_buy 개가 들어있는 카드팩 하나만 살 경우의 가격을 추가한다.
        
        이 가격들 중 최대가격을 구하면 된다.
        
        
        
        값들의 중복을 막기 위해 아래와 같은 범위설정을 한다.
        
        current_card_size_to_buy 가 홀수일 경우, 그리고 이를 2로 나누면 소수가 된다.
        이 값을 정수로 형변환 한 값 까지를 X로 설정하면 된다.
        ex) current_card_size_to_buy 가 5일 경우, X는 2까지
        
        current_card_size_to_buy 가 짝수일 경우, 그리고 이를 2로 나누면 정수이다.
        이 값 까지를 X로 설정하면 된다.
        ex) current_card_size_to_buy 가 6일 경우, X는 3까지
        
        '''

        for X in range(1, int(current_card_size_to_buy / 2) + 1):

            # 이전 단계의 조합들로 총 current_card_size_to_buy 개의 카드를 살 경우의 가격들을 구한다.
            possible_price_list.append(
                max_price_list_of_card_size[X]
                + max_price_list_of_card_size[current_card_size_to_buy - X]
            )

            print(possible_price_list)

            possible_price_list.append(Pi_list[current_card_size_to_buy])

        # max_price_list_of_card_size 의 값들 중 최대값이 현재 사려는 카드 개수를 살 때의 최대 지불 금액이다.
        max_price_list_of_card_size.append(max(possible_price_list))

        print()
        print()

    return max_price_list_of_card_size[N]


print(solution())
