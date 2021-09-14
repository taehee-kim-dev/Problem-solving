from itertools import product
import bisect


def solution(info, query):
    answer = []

    develop_languages = ['cpp', 'java', 'python', '']
    job_part = ['backend', 'frontend', '']
    career = ['junior', 'senior', '']
    soul_food = ['chicken', 'pizza', '']
    all_possible_queries = list(product(develop_languages, job_part, career, soul_food))

    query_person_dict = dict()
    for possible_query in all_possible_queries:
        possible_query = tuple([x for x in possible_query if x != ''])
        query_person_dict[possible_query] = []

    all_persons = []
    for one_person_info in info:
        one_person_info_split = one_person_info.split(' ')
        one_person_info_except_score = one_person_info_split[:-1]
        one_person_score = int(one_person_info_split[-1])
        all_persons.append(one_person_score)
        for possible_query_to_set in query_person_dict.keys():
            if set(possible_query_to_set).issubset(set(one_person_info_except_score)):
                scores_of_query = query_person_dict[possible_query_to_set]
                bisect.insort(scores_of_query, one_person_score)

    all_persons.sort()

    for one_query in query:
        count = 0
        one_query_split = one_query.split(' ')
        min_score_to_search = int(one_query_split[-1])
        query_to_search = tuple(x for x in one_query_split[:-1] if x != '-' and x != 'and')
        if query_to_search == '':
            index_to_insert = bisect.bisect_left(all_persons, min_score_to_search)
            count += len(all_persons) - index_to_insert
        else:
            searched_persons = query_person_dict[query_to_search]
            index_to_insert = bisect.bisect_left(searched_persons, min_score_to_search)
            count += len(searched_persons) - index_to_insert
        answer.append(count)
    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
print(solution(info, query))
