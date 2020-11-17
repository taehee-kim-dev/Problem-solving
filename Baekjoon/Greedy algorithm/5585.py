"""
거스름돈

500엔, 100엔, 50엔, 10엔, 5엔, 1엔 개수 무제한
거스름돈의 개수가 가장 적게 잔돈을 줌.
1000엔을 냄.
"""

answer_total_coin_count = 0

coins = [500, 100, 50, 10, 5, 1]

# 1 <= input_money < 1000 정수
input_money = int(input())

change = 1000 - input_money

for coin in coins:
    if change >= coin:
        answer_total_coin_count += int(change / coin)
        change %= coin

print(answer_total_coin_count)
