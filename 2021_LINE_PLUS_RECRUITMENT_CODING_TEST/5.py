






def solution(cards):

    answer = 0

    cards = [10 if x >= 11 else x for x in cards]

    while True:
        dealer = []
        player = []
        is_player_black_jack = False
        if len(cards) == 0:
            return answer
        player.append(cards.pop(0))
        if len(cards) == 0:
            return answer
        dealer.append(cards.pop(0))
        if len(cards) == 0:
            return answer
        player.append(cards.pop(0))
        if len(cards) == 0:
            return answer
        fourth_card = cards.pop(0)
        dealer.append(fourth_card)
        dealer_opened_card = fourth_card

        while 1 in player and sum(player) < 17:
            if sum(player) - 1 + 11 <= 21:
                index_of_one = player.index(1)
                player[index_of_one] = 11

        while 1 in dealer and sum(dealer) < 17:
            if sum(dealer) - 1 + 11 <= 21:
                index_of_one = dealer.index(1)
                dealer[index_of_one] = 11

        if sum(player) == 21:
            is_player_black_jack = True
        else:
            if dealer_opened_card == 1 or dealer_opened_card >= 7:
                while sum(player) < 17:
                    if len(cards) == 0:
                        return answer
                    player.append(cards.pop(0))
                    while 1 in player and sum(player) < 17:
                        if sum(player) - 1 + 11 <= 21:
                            index_of_one = player.index(1)
                            player[index_of_one] = 11
            elif dealer_opened_card == 4 or dealer_opened_card == 5 or dealer_opened_card == 6:
                pass
            else:
                while sum(player) < 12:
                    if len(cards) == 0:
                        return answer
                    player.append(cards.pop(0))
                    while 1 in player and sum(player) < 17:
                        if sum(player) - 1 + 11 <= 21:
                            index_of_one = player.index(1)
                            player[index_of_one] = 11

        while sum(dealer) < 17 and not is_player_black_jack:
            if len(cards) == 0:
                return answer
            dealer.append(cards.pop(0))
            while 1 in dealer and sum(dealer) < 17:
                if sum(dealer) - 1 + 11 <= 21:
                    index_of_one = dealer.index(1)
                    dealer[index_of_one] = 11

        if sum(dealer) > 21:
            answer += 2
        else:
            dealer_diff = 21 - sum(dealer)
            player_diff = 21 - sum(player)
            if dealer_diff == player_diff:
                pass
            elif player_diff < dealer_diff:
                if is_player_black_jack:
                    answer += 3
                else:
                    answer += 2
            else:
                answer -= 2




print(solution(
[1, 4, 10, 6, 9, 1, 8, 13]
))
# 1

print(solution(
[10, 13, 10, 1, 2, 3, 4, 5, 6, 2]
))
# -2

print(solution(
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
))
# -2

