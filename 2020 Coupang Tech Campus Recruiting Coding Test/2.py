def solution(n, customers):

    month_days = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    kiosk_last_finish_times = [None]
    kiosk_last_finish_times.extend([0 for _ in range(n)])
    kiosk_count = [None]
    kiosk_count.extend([0 for _ in range(n)])

    for one_customer_info in customers:
        month_and_day_str, time_str, running_time_str = one_customer_info.split()
        arrived_month, arrived_day = map(int, month_and_day_str.split('/'))
        arrived_hour, arrived_minute, arrived_sec = map(int, time_str.split(':'))
        running_time = int(running_time_str) * 60

        arrived_time_in_sec = sum(month_days[1:arrived_month]) * 24 * 3600 \
                              + (arrived_day - 1) * 24 * 3600 \
                              + arrived_hour * 3600 + arrived_minute * 60 + arrived_sec

        is_not_running_kiosk_exists = False
        not_running_kiosks = []
        running_kiosks = []
        for kiosk_number in range(1, n + 1):
            if kiosk_last_finish_times[kiosk_number] == 0 \
                    or kiosk_last_finish_times[kiosk_number] < arrived_time_in_sec:
                not_running_kiosks.append([kiosk_number, arrived_time_in_sec - kiosk_last_finish_times[kiosk_number]])
                is_not_running_kiosk_exists = True
            elif not is_not_running_kiosk_exists:
                running_kiosks.append([kiosk_number, kiosk_last_finish_times[kiosk_number]])

        if is_not_running_kiosk_exists:
            not_running_kiosks.sort(key=lambda x: -x[1])
            assigned_kiosk_number = not_running_kiosks[0][0]
            if kiosk_last_finish_times[assigned_kiosk_number] == 0:
                kiosk_last_finish_times[assigned_kiosk_number] = arrived_time_in_sec + running_time
            else:
                kiosk_last_finish_times[assigned_kiosk_number] = kiosk_last_finish_times[assigned_kiosk_number] + running_time

            kiosk_count[assigned_kiosk_number] += 1
        else:
            running_kiosks.sort(key=lambda x: x[1])
            assigned_kiosk_number = running_kiosks[0][0]
            if kiosk_last_finish_times[assigned_kiosk_number] == 0:
                kiosk_last_finish_times[assigned_kiosk_number] = arrived_time_in_sec + running_time
            else:
                kiosk_last_finish_times[assigned_kiosk_number] = kiosk_last_finish_times[assigned_kiosk_number] + running_time

            kiosk_count[assigned_kiosk_number] += 1

    return max(kiosk_count[1:])


print(solution(3,
               ["10/01 23:20:25 30", "10/01 23:25:50 26"]))
# 4

print(solution(2, ["02/28 23:59:00 03","03/01 00:00:00 02", "03/01 00:05:00 01"]))
# 2
