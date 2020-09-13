






def solution(ball, order):
    answer = []

    hold = []

    for ball_to_out in order:
        if ball[0] == ball_to_out:
            answer.append(ball.pop(0))
            while len(ball) > 0 and (ball[0] in hold or ball[-1] in hold):
                left_ball_in_hold_list = [x for x in hold if x == ball[0]]
                if len(left_ball_in_hold_list) > 0:
                    left_ball = left_ball_in_hold_list[0]
                    answer.append(ball.pop(0))
                    hold.remove(left_ball)

                right_ball_in_hold_list = [x for x in hold if x == ball[-1]]
                if len(right_ball_in_hold_list) > 0:
                    right_ball = right_ball_in_hold_list[0]
                    answer.append(ball.pop())
                    hold.remove(right_ball)

            continue

        if ball[-1] == ball_to_out:
            answer.append(ball.pop())
            while len(ball) > 0 and (ball[0] in hold or ball[-1] in hold):
                left_ball_in_hold_list = [x for x in hold if x == ball[0]]
                if len(left_ball_in_hold_list) > 0:
                    left_ball = left_ball_in_hold_list[0]
                    answer.append(ball.pop(0))
                    hold.remove(left_ball)

                right_ball_in_hold_list = [x for x in hold if x == ball[-1]]
                if len(right_ball_in_hold_list) > 0:
                    right_ball = right_ball_in_hold_list[0]
                    answer.append(ball.pop())
                    hold.remove(right_ball)
            continue

        hold.append(ball_to_out)

    return answer






# print(solution(
# [1, 2, 3, 4, 5, 6], [6, 2, 5, 1, 4, 3]
# ))
# # [6, 5, 1, 2, 4, 3]

print(solution(
[11, 2, 9, 13, 24], [9, 2, 13, 24, 11]
))
# [24, 13, 9, 2, 11]

