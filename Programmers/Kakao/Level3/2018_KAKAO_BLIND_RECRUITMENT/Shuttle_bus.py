"""
셔틀버스
"""


def solution(n, t, m, timetable):

    # 콘이 셔틀버스를 탈 수 있는 시간들 중 가장 늦은 시간
    con_time = -1

    # 셔틀버스 도착 시작시간 9:00를 분단위로 변환
    shuttle_bus_start_time_in_minutes = 9 * 60
    # 셔틀버스가 도착하는 시간들 분단위로 저장
    shuttle_bus_timetable_in_minutes = []
    # 셔틀버스는 n회 운행
    for count in range(n):
        # 셔틀버스 도착 시간 계산
        shuttle_bus_time = shuttle_bus_start_time_in_minutes + (t * count)
        shuttle_bus_timetable_in_minutes.append(shuttle_bus_time)

    # 대기열에 서있는 크루들 도착시간 분단위로 저장
    waiting_crew_time = []
    for time in timetable:
        hours, minutes = map(int, time.split(':'))
        time_in_minutes = hours * 60 + minutes
        waiting_crew_time.append(time_in_minutes)

    # 크루들 도착시간 입력값이 순서가 뒤죽박죽이므로, 오름차순으로 정렬
    waiting_crew_time.sort()

    """
    무조건 막차의 마지막 순서로 탄다.
    콘을 제외하고 크루들만 버스를 타는 경우를 생각해 본다.
    
    막차가 크루틀로 꽉차면, 마지막으로 탑승하는 크루보다 1분 빨리 도착해야 한다.
    막차가 콘이 없어도 크루들로 꽉차는데 콘이 마지막으로 탄 크루와 같은 시간에 도착하면
    문제설명에 따라 같은 시각에 도착한 크루 중 대기열에서 제일 뒤에 서게 되므로 
    막차를 타지 못한다.
    
    막자가 크루들로 꽉차지 않으면, 버스 도착시간에 도착해도 탑승할 수 있다. 
    """
    # 셔틀버스의 도착시간이 이른순서대로 차례대로 탑승처리
    for bus_index, bus_time in enumerate(shuttle_bus_timetable_in_minutes):
        # 현재 탑승처리중인 버스에 탑승한 사람 수
        number_of_people_on_the_bus = 0
        # 현재 탑승처리중인 버스에 탑승한 크루들의 도착시간
        crew_time_on_the_bus = []
        # 크루들 버스 탑승
        # 버스 도착시간을 포함하여 이전에 온 크루들만 버스탑승의 1차적 고려대상이 될 수 있다.
        for crew_time in [crew_time for crew_time in waiting_crew_time if crew_time <= bus_time]:
            if number_of_people_on_the_bus < m:
                # 버스에 자리가 남아있어야 버스에 탈 수 있다.
                # 현재 버스에 탑승한 크루들의 도착시간을 저장한다.
                crew_time_on_the_bus.append(crew_time)
                # 현재 버스에 탑승한 사람 수를 1 증가시킨다.
                number_of_people_on_the_bus += 1

        # 버스에 탑승한 크루들의 수 만큼 대기열에 서있는 크루들의 맨 앞부터 삭제
        waiting_crew_time = waiting_crew_time[number_of_people_on_the_bus:]

        # 현재 탑승처리를 한 버스가 막차일 때
        if bus_index == len(shuttle_bus_timetable_in_minutes) - 1:
            if number_of_people_on_the_bus == m:
                # 만약 막차가 크루들로 꽉찼으면
                # 콘은 마지막에 탑승한 크루의 도착시간보다 1분 더 일찍 도착해야 한다.
                con_time = crew_time_on_the_bus[-1] - 1
            else:
                # 만약 막차가 꽉차지 않았으면
                # 콘은 버스 도착시간에 도착해도 탑승할 수 있다.
                con_time = bus_time

    # 단위가 분이므로 시간과 분 단위로 나눈다.
    # 정답 문자열 형식에 맞게 조합하여 반환한다.
    return '{}:{}'.format(str(con_time // 60).zfill(2), str(con_time % 60).zfill(2))
