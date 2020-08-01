"""
[1차] 캐시
"""


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    answer = 0
    lower_case_cities = [x.lower() for x in cities]
    cache = []

    for city in lower_case_cities:
        if city in cache:
            answer += 1
            del cache[cache.index(city)]
            cache.append(city)
        else:
            answer += 5
            if len(cache) == cacheSize:
                del cache[0]
            cache.append(city)
    return answer


print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))

