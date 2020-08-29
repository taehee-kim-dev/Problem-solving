"""
상금 헌터
"""

T = int(input())

for _ in range(T):
    a, b = map(int, input().split(' '))
    a_reward = 0
    b_reward = 0
    if a == 0:
        a_reward = 0
    elif a == 1:
        a_reward = 500
    elif 2 <= a <= 3:
        a_reward = 300
    elif 4 <= a <= 6:
        a_reward = 200
    elif 7 <= a <= 10:
        a_reward = 50
    elif 11 <= a <= 15:
        a_reward = 30
    elif 16 <= a <= 21:
        a_reward = 10

    if b == 0:
        b_reward = 0
    if b == 1:
        b_reward = 512
    elif 2 <= b <= 3:
        b_reward = 256
    elif 4 <= b <= 7:
        b_reward = 128
    elif 8 <= b <= 15:
        b_reward = 64
    elif 16 <= b <= 31:
        b_reward = 32

    print((a_reward + b_reward) * 10000)
