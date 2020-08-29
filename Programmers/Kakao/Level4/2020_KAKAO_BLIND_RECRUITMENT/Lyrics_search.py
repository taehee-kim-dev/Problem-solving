"""
가사 검색
"""


def search(words, current_keyword_front_question_mark, pure_current_keyword, current_keyword):
    if current_keyword_front_question_mark:
        # 물음표가 앞에서부터 있을 때
        return [x for x in words if x.endswith(pure_current_keyword) and len(x) == len(current_keyword)]
    else:
        # 물음표가 뒤에서부터 있을 때
        return [x for x in words if x.startswith(pure_current_keyword) and len(x) == len(current_keyword)]


def solution(words, queries):
    answer = []

    queries_duplicate_removed = list(set(queries))
    queries_duplicate_removed.sort(key=lambda x: [x, -x.count('?')])
    # [결과 갯수, 결과]
    search_keyword_results = dict.fromkeys(queries_duplicate_removed)
    for keyword in queries_duplicate_removed:
        search_keyword_results[keyword] = {'result': [], 'number_of_result': 0}
    # 기본 사전순 정렬. 사전순이 같다면, 물음표가 많은 순서대로 정렬.
    for current_keyword_index, current_keyword in enumerate(queries_duplicate_removed):

        # 물음표가 앞쪽에 있는지, 뒷쪽에 있는지
        current_keyword_front_question_mark = True if current_keyword.startswith('?') else False
        current_keyword_question_mark_index = current_keyword.rfind('?') if current_keyword_front_question_mark else current_keyword.find('?')
        pure_current_keyword = current_keyword[current_keyword_question_mark_index + 1:] if current_keyword_front_question_mark else current_keyword[:current_keyword_question_mark_index]
        """
        현재 키워드와 형태가 겹치면서 물음표가 더 많은 키워드가 있는지 검사
        현재 키워드가 같은 형태에서 가장 물음표가 많은 키워드라면 그냥 검사.
        물음표가 많은 키워드를 먼저 검색하고 결과 저장.
        같은 형태이면서 물음표가 더 적은 키워드는 저장된 상위 키워드의 결과에서 다시 검색.
        """

        # 처음 검사하는 키워드가 아니면
        before_keyword = queries_duplicate_removed[current_keyword_index - 1]
        same_format = before_keyword.endswith(pure_current_keyword) if current_keyword_front_question_mark else before_keyword.startswith(pure_current_keyword)
        if same_format and current_keyword_index != 0:
            if before_keyword.startswith(pure_current_keyword):
                # 만약 직전에 검사한 키워드가 같은 형태라면
                # 직전 검사 키워드 결과에서 검사함.
                before_search_result = search_keyword_results[before_keyword]['result']
                search_keyword_results[current_keyword]['result'] = search(before_search_result, current_keyword_front_question_mark, pure_current_keyword, current_keyword)
                search_keyword_results[current_keyword]['number_of_result'] = len(search_keyword_results[current_keyword]['result'])

        # 처음 검사하는 키워드이거나 직전에 검사한 키워드가 다른 형태라면
        # 전체 가사 단어에서 검색함.
        search_keyword_results[current_keyword]['result'] = search(words, current_keyword_front_question_mark, pure_current_keyword, current_keyword)
        search_keyword_results[current_keyword]['number_of_result'] = len(search_keyword_results[current_keyword]['result'])

    for keyword in queries:
        answer.append(search_keyword_results[keyword]['number_of_result'])

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
# [3, 2, 4, 1, 0]
