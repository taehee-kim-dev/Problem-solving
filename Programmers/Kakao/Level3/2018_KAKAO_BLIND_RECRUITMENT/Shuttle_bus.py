"""
셔틀버스
"""

from copy import deepcopy


def make_timetable_with_con(crew_timetable_in_minutes, con_time):
    timetable = deepcopy(crew_timetable_in_minutes)
    # 마지막에 콘을 넣을 때 비교를 위해 매우 큰 시간 값 삽입
    timetable.append((2000000000, 'last'))
    ret = []
    before_crew_time = 0
    for crew in timetable:
        # 시간 순서대로 서되,
        # 같은 도착시간의 크루들이 있을때는 그들의 맨 뒤에 선다.
        if before_crew_time <= con_time < crew[0]:
            ret.append((con_time, 'con'))
        ret.append(crew)
        before_crew_time = crew[0]

    return ret


def con_get_on_the_bus(bus_time, timetable_with_con, m, con_time):
    # 버스가 도착했을 때,
    # 버스 도착 시간을 포함한 이전에 줄울 서 있는 사람들 중에
    save_time_crew = [crew for crew in timetable_with_con if crew[0] <= bus_time]
    # m명만 버스를 탈 수 있다.
    crew_who_can_get_on_the_bus = save_time_crew[:m]
    # 버스를 탑승한 크루들은 리스트에서 제거한다.
    for crew in crew_who_can_get_on_the_bus:
        timetable_with_con.remove(crew)
    # 버스에 탑승한 크루들 중에 콘이 포함되어있는지 여부 반환
    return (con_time, 'con') in crew_who_can_get_on_the_bus


def solution(n, t, m, timetable):
    # 고려해 봐야 하는 콘의 셔틀 대기열 도착시간들
    timetable_of_con = []
    # 셔틀버스 도착 시작시간 9:00를 분단위로 변환
    shuttle_bus_start_time_in_minutes = 9 * 60
    # 셔틀버스가 도착하는 시간들
    shuttle_bus_timetable_in_minutes = []
    # 셔틀버스는 n회 운행
    for count in range(n):
        # 셔틀버스 도착 시간 계산
        shuttle_bus_time = shuttle_bus_start_time_in_minutes + (t * count)
        shuttle_bus_timetable_in_minutes.append(shuttle_bus_time)
        # 콘이 셔틀버스 도착 시간에 도착하는 경우를 고려한다.
        timetable_of_con.append(shuttle_bus_time)
    # 크루들 도착시간
    crew_timetable_in_minutes = []
    for index, time in enumerate(timetable):
        hours, minutes = map(int, time.split(':'))
        total_minutes = hours * 60 + minutes
        crew_timetable_in_minutes.append((total_minutes, 'crew{}'.format(index)))
        # 콘이 각 크루들의 도착시간 1분 전에 도착하는 경우를 고려한다.
        timetable_of_con.append(total_minutes - 1)

    # 크루들 도착시간 오름차순 정렬
    crew_timetable_in_minutes.sort(key=lambda x: x[0])
    # 고려하는 콘의 도착시간 모든 경우 오름차순 정렬
    timetable_of_con = list(set(timetable_of_con))
    timetable_of_con.sort()
    # 콘이 버스를 탈 수 있는 도착시간들
    time_con_can_get_on_the_bus = []

    # 고려하는 콘의 도착시간의 경우를 하나씩 검사
    for con_time in timetable_of_con:
        # 크루들의 도착시간에 콘의 도착시간을 끼워넣는다.
        timetable_with_con = make_timetable_with_con(crew_timetable_in_minutes, con_time)
        # 버스가 도착하는 시간들을 하나씩 검사
        for bus_time in shuttle_bus_timetable_in_minutes:
            # 콘이 이 조건에서 버스를 탈 수 있는가?
            if con_get_on_the_bus(bus_time, timetable_with_con, m, con_time):
                # 탈 수 있으면, 콘이 버스를 탈 수 있는 도착시간들을 저장하는 리스트에 저장
                time_con_can_get_on_the_bus.append(con_time)
                break

    # 콘이 버스를 탈 수 있는 도착시간들 중에 가장 늦은 도착시간을 꺼내서
    latest_time = sorted(time_con_can_get_on_the_bus)[-1]
    # 단위가 분이므로 시간과 분 단위로 나눈다.
    hours = str(latest_time // 60)
    minutes = str(latest_time % 60)
    # 정답 문자열 형식에 맞게 조합하여 반환한다.
    return '{}:{}'.format(hours.zfill(2), minutes.zfill(2))



#print(solution(1, 1, 5, ['08:00', '08:01', '08:02', '08:03']))
print(solution(10, 60, 10, ["17:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
