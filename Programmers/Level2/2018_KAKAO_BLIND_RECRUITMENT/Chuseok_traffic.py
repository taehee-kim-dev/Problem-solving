from decimal import Decimal

"""
1[차] 추석 트래픽

1초 구간 동안, 처리중인 task의 수가 가장 많을 때의 task 수를 구해야 한다.
"""


class Task:
    def __init__(self, initial_request_time_in_milli_seconds, response_end_time_in_milli_seconds):
        self.initial_request_time_in_milli_seconds = initial_request_time_in_milli_seconds
        self.response_end_time_in_milli_seconds = response_end_time_in_milli_seconds

    def is_on_processing(self, start_time, end_time):
        return (not self.response_end_time_in_milli_seconds < start_time) and (not end_time < self.initial_request_time_in_milli_seconds)


def solution(lines):
    answer = 0
    tasks = []
    times = []
    for line in lines:
        log = line.split(" ")

        response_end_time = log[1]
        response_end_hours, response_end_minutes, response_end_seconds = map(Decimal, response_end_time.split(':'))
        response_end_time_in_seconds = Decimal('3600') * response_end_hours + Decimal('60') * response_end_minutes + response_end_seconds

        processing_time = log[2]
        processing_time = Decimal(processing_time[:-1])

        initial_request_time_in_seconds = response_end_time_in_seconds - processing_time + Decimal('0.001')

        response_end_time_in_milli_seconds = int(Decimal('1000') * response_end_time_in_seconds)
        initial_request_time_in_milli_seconds = int(Decimal('1000') * initial_request_time_in_seconds)

        tasks.append(Task(initial_request_time_in_milli_seconds, response_end_time_in_milli_seconds))

        times.append(response_end_time_in_milli_seconds)

    times = list(set(times))
    times.sort()

    for start_time_in_range_of_one_second in times:
        end_time_in_range_of_one_second = start_time_in_range_of_one_second + 999
        current_tasks = len(list(filter(lambda task: task.is_on_processing(start_time_in_range_of_one_second, end_time_in_range_of_one_second), tasks)))
        if current_tasks > answer:
            answer = current_tasks
    return answer

