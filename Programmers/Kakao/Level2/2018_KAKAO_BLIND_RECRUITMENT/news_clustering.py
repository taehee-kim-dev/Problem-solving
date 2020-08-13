import re
from collections import Counter


def solution(str1, str2):
    answer = 0

    # 문자열들을 모두 소문자로 변환
    str1 = str1.lower()
    str2 = str2.lower()

    multiset1 = Counter()
    multiset2 = Counter()

    # 두 글자씩 끊어서 multiset에 추가.
    # 단, 글자중에서 둘다 영문자가 아니면 버림.

    # 길이가 2인 문자열의 두 문자가 모두 알파벳인 정규표현식
    str_pattern = re.compile("^[a-zA-Z]{2}$")

    # str1의 문자를 맨 앞부터 2개씩 검사
    for i in range(len(str1) - 1):
        tmp_str = str1[i:i+2]
        # 정규표현식에 부합하면,
        if str_pattern.match(tmp_str) is not None:
            # multiset1에 추가
            multiset1.update([tmp_str])

    # str2의 문자를 맨 앞부터 2개씩 검사
    for i in range(len(str2) - 1):
        tmp_str = str2[i:i+2]
        # 정규표현식에 부합하면,
        if str_pattern.match(tmp_str) is not None:
            # multiset2에 추가
            multiset2.update([tmp_str])

    # 교집합
    intersection = multiset1 & multiset2
    # 합집합
    union = multiset1 | multiset2

    intersection_size = 0
    for element, size in intersection.items():
        intersection_size += size

    union_size = 0
    for element, size in union.items():
        union_size += size

    # 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니
    # 따로 J(A, B) = 1로 정의한다.
    if intersection_size == 0 and union_size == 0:
        return 65536

    return int(intersection_size / union_size * 65536)
