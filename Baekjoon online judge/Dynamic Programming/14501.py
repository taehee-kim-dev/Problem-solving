"""
퇴사

i = 상담 날짜
Ti = i 번째 날짜부터 시작한 상담을 완료하는데 걸리는 일 수
Pi = i 번째 날짜부터 상담을 시작했을 때 해당 상담에 대해 받는 금액

하나의 상담을 잡으면 끝날 때 까지 다른 상담을 못함.
상담이 끝나는 날짜가 N일 이후에 끝나면 해당 상담은 잡을 수 없음.

상담을 적절히 해서 얻을 수 있는 최대 수익은?
"""

# 1 <= N <= 15
N = int(input())

Ti = [0 for _ in range(N + 1)]
Pi = [0 for _ in range(N + 1)]

# dp_max_income[day_i] = day_i일 까지 얻을 수 있는 최대 수익
dp_max_income_up_to_day_i = [0 for _ in range(N + 1)]

# 입력
for day_i in range(1, N + 1):
    # (1 <= Ti <= 5, 1 <= Pi <= 1000)
    T_input, P_input = map(int, input().split(' '))
    Ti[day_i] = T_input
    Pi[day_i] = P_input


for day_i in range(1, N + 1):
    
    # N일 이내에 종료되는 상담만 상담할 수 있다.
    if N >= day_i + Ti[day_i] - 1:
        # day_i일의 상담을 했을 경우,
        # 해당 상담이 종료되는 날의 수익을 최대값으로 갱신한다.
        # max(해당 상담 종료 날짜의 기존 최대값, 해당 상담을 했을 때의 종료 날짜의 수익 최대값)
        dp_max_income_up_to_day_i[day_i + Ti[day_i] - 1] \
            = max(dp_max_income_up_to_day_i[day_i + Ti[day_i] - 1],
                  dp_max_income_up_to_day_i[day_i - 1] + Pi[day_i])

    # day_i일의 상담을 하지 않을 경우
    dp_max_income_up_to_day_i[day_i] = max(dp_max_income_up_to_day_i[day_i - 1],
                                           dp_max_income_up_to_day_i[day_i])

        
print(dp_max_income_up_to_day_i[-1])
