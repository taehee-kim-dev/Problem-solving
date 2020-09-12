



class UserPlayTime:
    def __init__(self):
        self.start_time_in_sec = 0
        self.end_time_in_sec = 0


def solution(play_time, adv_time, logs):

    if play_time == adv_time:
        return '00:00:00'
    answer = ''
    answer_times = []
    all_users_play_times = []
    log_times = []
    for log in logs:
        start_time, end_time = log.split('-')
        start_hour, start_min, start_sec = start_time.split(':')
        start_time_in_sec = int(start_hour) * 3600 + int(start_min) * 60 + int(start_sec)
        end_hour, end_min, end_sec = end_time.split(':')
        end_time_in_sec = int(end_hour) * 3600 + int(end_min) * 60 + int(end_sec)
        log_times.append(['start', start_time_in_sec])
        log_times.append(['end', end_time_in_sec])
        user_play_time = UserPlayTime()
        user_play_time.start_time_in_sec = start_time_in_sec
        user_play_time.end_time_in_sec = end_time_in_sec
        all_users_play_times.append(user_play_time)

    log_times.sort(key=lambda x: x[1])

    adv_time_hour, adv_time_min, adv_time_sec = map(int, adv_time.split(':'))
    adv_time_in_sec = adv_time_hour * 3600 + adv_time_min * 60 + adv_time_sec

    for log_time in log_times:
        if log_time[0] == 'start':
            adv_start_time = log_time[1]
            adv_end_time = adv_start_time + adv_time_in_sec
            user_play_times = [x for x in all_users_play_times if not (x.end_time_in_sec <= adv_start_time
                                                                       or x.start_time_in_sec >= adv_end_time)]
            all_time = 0
            for play_time in user_play_times:
                if play_time.start_time_in_sec <= adv_start_time \
                    and play_time.end_time_in_sec >= adv_end_time:
                    all_time += adv_time_in_sec
                elif adv_start_time < play_time.start_time_in_sec \
                    and play_time.end_time_in_sec < adv_start_time:
                    all_time += (play_time.end_time_in_sec - play_time.start_time_in_sec)
                elif play_time.start_time_in_sec < adv_start_time \
                    and play_time.end_time_in_sec < adv_end_time:
                    all_time += (play_time.end_time_in_sec - adv_start_time)
                elif play_time.start_time_in_sec < adv_end_time \
                    and adv_end_time < play_time.end_time_in_sec:
                    all_time += (adv_end_time - play_time.start_time_in_sec)

            answer_times.append([all_time, adv_start_time])


    answer_times.sort(key=lambda x: [-x[0], x[1]])
    answer_time = answer_times[0][1]
    answer_hour = 0
    answer_min = 0
    answer_sec = 0
    answer_hour = answer_time // 3600
    if answer_hour > 0:
        answer_time %= 3600
    answer_min = answer_time // 60
    if answer_min > 0:
        answer_sec = answer_time % 60
    answer_hour = str(answer_hour)
    answer_min = str(answer_min)
    answer_sec = str(answer_sec)
    answer = answer_hour.zfill(2) + ':' + answer_min.zfill(2) + ':' + answer_sec.zfill(2)
    return answer









print(solution(
"02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
))
# "01:30:59"

print(solution(
"99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
))
# "01:00:00"

print(solution(
"50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
))
# "00:00:00"