from copy import deepcopy


class Person:
    def __init__(self):
        self.language = ''
        self.part = ''
        self.year = ''
        self.soul_food = ''
        self.score = 0



def solution(info, query):
    answer = []

    all_persons = []
    for person in info:
        language, part, year, soul_food, score = person.split(' ')
        new_person = Person()
        new_person.language = language
        new_person.part = part
        new_person.year = year
        new_person.soul_food = soul_food
        new_person.score = int(score)
        all_persons.append(new_person)

    for one_query in query:
        query_split = one_query.split(' ')
        query_split = [x for x in query_split if not(x == '-' or x == 'and')]
        language = None
        part = None
        year = None
        soul_food = None
        score = None
        for q in query_split:
            if q == 'cpp' or q == 'java' or q == 'python':
                language = q
            elif q == 'backend' or q == 'frontend':
                part = q
            elif q == 'junior' or q == 'senior':
                year = q
            elif q == 'chicken' or q == 'pizza':
                soul_food = q
            else:
                score = int(q)

        query_result = deepcopy(all_persons)
        if language is not None:
            query_result = [x for x in query_result if x.language == language]

        if part is not None:
            query_result = [x for x in query_result if x.part == part]

        if year is not None:
            query_result = [x for x in query_result if x.year == year]

        if soul_food is not None:
            query_result = [x for x in query_result if x.soul_food == soul_food]

        if score is not None:
            query_result = [x for x in query_result if x.score >= score]

        answer.append(len(query_result))

    return answer










print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
# [1,1,1,1,2,4]
