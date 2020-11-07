import collections
"""
부정행위 의심자의 수험번호를(문자열 형태) 사전 순으로 정렬
단, 부정행위자로 의심되는 수험자가 없는 경우에는 문자열 'None'을 배열에 담아 return
"""


def solution(logs):
    answer = []

    """
    수험번호 문제번호 점수
    문제를 풀지 않은 경우는 logs에 기록되지 않습니다.
    0점을 받는 답안 제출도 문제를 푼 것으로 칩니다.
    단, 마지막 제출의 채점 결과가 최종 점수입니다.
    """
    exam_results_map = collections.defaultdict(dict)

    for log in logs:
        person_number, question_number, score = log.split()
        exam_results_map[person_number][question_number] = score

    exam_results_set_map = collections.defaultdict(set)
    for person_number, result in exam_results_map.items():
        if len(result) >= 5:
            for question_number, score in result.items():
                exam_results_set_map[person_number].add((question_number, score))

    testers = list(exam_results_set_map.keys())
    for i in range(0, len(testers) - 1):
        for j in range(i + 1, len(testers)):
            if exam_results_set_map[testers[i]] == exam_results_set_map[testers[j]]:
                if testers[i] not in answer:
                    answer.append(testers[i])
                if testers[j] not in answer:
                    answer.append(testers[j])

    if not answer:
        return ['None']
    else:
        return sorted(answer)

solution(["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "2001 1 100", "2001 2 100", "2001 4 100", "2001 7 95", "2001 9 100", "2002 1 95", "2002 2 100", "2002 4 100", "2002 7 100", "2002 9 100"])