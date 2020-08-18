import re
from itertools import product

"""
불량 사용자
당첨에서 제외되어야 할 제재 아이디 목록은 몇가지 경우의 수가 가능한 지?
"""


# 정규식 패턴을 만드는 함수
def make_pattern(banned_id_format):
    # 문자열 시작 매칭 기호를 맨 앞에 붙여준다.
    pattern = '^'
    # 불량 아이디 형식 문자열의 문자를 하나씩 본다.
    for character in banned_id_format:
        # 문자가 만약 '*'라면, 소문자 알파벳, 숫자 중 한 문자가 올 수 있다.
        if character == '*':
            pattern += '[a-z0-9]{1}'
        else:
            # 그게 아니라면 해당 문자나, 숫자가 꼭 와야 한다.
            pattern += character
    # 문자열 끝 매칭 기호를 맨 뒤에 붙여준다.
    pattern += '$'
    # 만든 패턴 반환
    return pattern


def solution(user_id, banned_id):
    # 각 불량 아이디 형식에 해당하는 아이디들을 모두 저장할 리스트
    # 2차원 리스트이며, 한 row에는 한 불량 아이디 형식에 해당되는 유저 아이디들이 list 안에 담겨진다.
    banned_user_ids = []

    # 매개변수로 입력받은 불량 아이디 형식들 중 하나씩 형식을 꺼낸다.
    for banned_id_format in banned_id:
        # 정규식 패턴을 만드는 함수를 호출한다.
        pattern = make_pattern(banned_id_format)
        # 만든 정규식 패턴 문자열을 패턴 객체로 컴파일한다.
        banned_id_format_pattern = re.compile(pattern)
        # 현재 검사하고 있는 불량 아이디 형식에 해당되는 아이디들을 담을 리스트
        pattern_matched_user_ids = []
        # 매개변수로 입력받은 모든 유저아이디들을 하니씩 검사한다.
        for one_user_id in user_id:
            # 현재 검사한 유저아이디가 현재 검사중인 불량 아이디 형식에 해당하는지 매칭해본다.
            match_result = banned_id_format_pattern.match(one_user_id)
            # 매칭 결과가 일치하다고 나오면 (불일치일 경우 None 반환)
            if match_result is not None:
                # 위에서 선언한 현재 검사하고 있는 패턴에 매칭된
                # 유저 아이디들을 저장하는 리스트에 추가한다.
                pattern_matched_user_ids.append(one_user_id)

        # pattern_matched_user_ids에 있는 유저 아이디들은
        # 현재 검사한 불량 아이디 형식에 해당하는 불량 사용자들이므로 맨 앞에 선언한 리스트에 추가한다.
        banned_user_ids.append(pattern_matched_user_ids)

    # 각 불량 아이디 형식에 해당하는 유저 아이디들의 중복을 허용하여
    # 가능한 모든 조합의 제재 아이디 목록을 생성한다.
    duplicate_allowed_all_cases = list(product(*banned_user_ids))
    # 중복을 제거한 제재 아이디 목록들을 저장할 리스트를 선언한다.
    duplicate_removed_cases = []
    # 중복이 허용된 제재 아이디 목록의 모든 케이스들에서 하나의 케이스씩 꺼내서 검사한다.
    for case in duplicate_allowed_all_cases:
        # 한 케이스의 제재 아이디 목록에서 set 변환을 이용해 중복된 아이디들을 제거한다.
        duplicate_removed_one_case = set(case)

        # 제재 아이디 목록에 중복된 원소가 없다면,
        # set으로 변환했을 때의 길이와 원래 목록의 길이가 같고,
        # 중복된 원소가 있다면 다르다.
        # 중복된 원소가 있으면 버리고 다음 케이스를 검사한다.
        if len(case) != len(duplicate_removed_one_case):
            continue

        # 위에서 중복을 허용하여 가능한 모든 제재 아이디 목록을 생성할 때,
        # 각 불량 아이디 형식에 해당하는 유저 아이디들 중 하나씩 선택하여
        # 제재 아이디 목록을 만드는 것이기 때문에
        # 2개 이상의 아이디(예: a, b, c)들이 2개 이상의 불량 아이디 형식들에 해당 될 경우,
        # 만들어진 제재 아이디 목록은 튜플 형이므로 순서에 따라 다르게 인식되어
        # 한 목록 안의 중복된 아이디들을 위에서 set으로 변환해 제거하더라도,
        # (a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)
        # 위와같이 생성된 목록들이 중복될 수 있다.
        # 따라서 set으로 변환해 순서에 무관하게 만든 후, duplicate_removed_cases에 저장하여,
        # 다음 제재 목록을 검사할 때, 이미 같은 set이 duplicate_removed_cases에 존재하지 않는지 검사하여
        # 중복된 아이디는 없지만 아이디들의 순서만 달라 목록들이 중복되는 경우를 막는다.
        if duplicate_removed_one_case not in duplicate_removed_cases:
            # 현제 제재 아이디 목록 안에 중복된 아이디가 없고,
            # 이 제재 아이디 목록이 중복을 제거한 제재 아이디 리스트에 없다면,
            # 중복을 제거한 제재 아이디 리스트에 추가한다.
            duplicate_removed_cases.append(duplicate_removed_one_case)

    # 중복을 제거한 제재 아이디 리스트의 길이가
    # 중복을 허용하지 않았을 때 가능한 제재 아이디 리스트의 모든 경우의 수이다.
    return len(duplicate_removed_cases)
