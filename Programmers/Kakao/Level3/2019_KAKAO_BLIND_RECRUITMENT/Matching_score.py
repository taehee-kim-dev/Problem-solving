"""
매칭 점수
"""

import re
from copy import deepcopy
from decimal import Decimal


# 웹페이지 객체 생성
class Page:
    def __init__(self, index):
        # 인덱스
        self.index = index
        # 자기 자신의 주소
        self.main_link = ''
        # 기본점수 : 검색어 등장 횟수
        self.basic_score = Decimal('0')
        # 외부 링크
        self.external_links = []
        # 외부 링크 개수
        self.number_of_external_links = Decimal('0')
        # 링크점수 : (이 웹페이지를 참조하는 외부 페이지의 기본점수 / 이 웹페이지를 참조하는 외부 페이지의 외부 링크 수)의 총합
        self.link_score = Decimal('0')
        # 매칭점수 : 기본점수 + 링크점수
        self.matching_score = Decimal('0')


# 페이지 메인주소 구하기
def get_main_link(page):
    # 페이지 복사
    page_for_main_link = deepcopy(page)
    
    # head 태그 내용 시작점 찾기
    head_start = page_for_main_link.find('<head>') + 6
    # head 태그 내용 끝점 찾기
    head_end = page_for_main_link[head_start:].find('</head>') + head_start
    # head 태그 내용 추출
    head = page_for_main_link[head_start:head_end]

    while True:
        # meta 태그 시작점 찾기
        meta_start = head.find('<meta')
        # meta 태그 없으면 break
        if meta_start == -1:
            break
        # meta 태그 내용 시작점 찾기
        meta_start += 5
        # meta 태그 내용 끝점 찾기
        meta_end = head[meta_start:].find('>') + meta_start
        # meta 태그 추출
        meta = head[meta_start:meta_end]
        # meta 태그에 아래 두 속성 있어야만 함
        if meta.find('property=\"og:url\"') != -1 \
                or meta.find('content=\"https://') != -1:
            # 메인주소 시작점 찾기
            main_url_start = meta.find('content=\"https://') + 17
            # 메인주소 끝점 찾기
            main_url_end = meta[main_url_start:].find('\"') + main_url_start
            # 메인주소 추출
            main_url = meta[main_url_start:main_url_end]
            # 메인주소 반환
            return main_url
        
        # 없으면 방금 검사한 곳 이후부터 다시검사
        head = head[meta_end + 1:]
        continue

    return


# 외부 링크들 구하기
def get_external_links(page):
    # 페이지 복사
    page_for_external_links = deepcopy(page)
    # 외부 링크들을 저장할 리스트
    all_external_links = []
    while True:
        # a 태그 시작점 찾기
        a_start = page_for_external_links.find('<a')
        # a 태그 없으면 break
        if a_start == -1:
            break
        # a 태그 내용 시작점 설정
        a_start += 2
        # a 태그 내용 끝점 찾기
        a_end = page_for_external_links[a_start:].find('>') + a_start
        # a 태그 추출
        a = page_for_external_links[a_start:a_end]
        # a 태그 href 속성의 외부링크 시작점 찾기
        external_link_start = a.find('href=\"https://') + 14
        # a 태그 href 속성의 외부링크 끝점 찾기
        external_link_end = a[external_link_start:].find('\"') + external_link_start
        # 외부링크 추출
        external_link = a[external_link_start:external_link_end]
        # 리스트에 저장
        all_external_links.append(external_link)
        # 방금 검사한 곳 이후부터 재검사
        page_for_external_links = page_for_external_links[a_end + 1:]

    # 외부링크 리스트 반환
    return all_external_links


# 페이지 기본점수 구하기
def get_basic_score(page, word):
    """
    페이지의 모든 알파벳 소문자로 변환
    찾을 단어도 소문자로 변환
    알파벳을 제외한 모든 문자를 '.'으로 변환
    '.'을 기준으로 split을 하면
    알파벳을 제외한 모든 문자 사이에 있던 단어들이 추출된다.
    해당 리스트에서 단어의 개수를 반환한다.
    """
    return Decimal(str(re.sub('[^a-z]', '.', page.lower()).split('.').count(word.lower())))


def solution(word, pages):
    # 모든 페이지 객체들을 담을 리스트
    all_page_objects = []

    # 페이지를 하나씩 꺼낸다
    for index, page in enumerate(pages):
        # 인덱스를 생성자 매개변수로 넘겨주면서 페이지 객체를 생성
        new_page = Page(index)
        # 이 페이지의 메인주소를 구해서 저장
        new_page.main_link = get_main_link(page)
        # 이 페이지가 참조하는 외부링크들을 모두 구해서 저장
        new_page.external_links = get_external_links(page)
        # 이 페이지가 참조하는 외부링크들의 개수 저장
        new_page.number_of_external_links = Decimal(str(len(new_page.external_links)))
        # 이 페이지의 기본점수 구해서 저장
        new_page.basic_score = get_basic_score(page, word)
        # 페이지 객체 저장
        all_page_objects.append(new_page)

    # 모든 객체 리스트에서 참조되는 페이지 객체를 하나씩 꺼낸다.
    for referenced_page in all_page_objects:
        # 이 페이지를 외부링크로 참조하고있는 모든 페이지 객체들을 가져온다.
        all_referencing_pages = [page for page in all_page_objects if referenced_page.main_link in page.external_links]
        # 이 페이지를 참조하고있는 페이지 객체를 하나씩 꺼낸다.
        for referencing_page in all_referencing_pages:
            # 참조되는 페이지 객체의 링크점수를 계산해서 업데이트한다.
            referenced_page.link_score += referencing_page.basic_score / referencing_page.number_of_external_links
        # 참조되는 페이지 객체의 링크점수 업데이트가 모두 끝났으면, 매칭점수를 계산해 설정한다.
        referenced_page.matching_score = referenced_page.basic_score + referenced_page.link_score

    # 모든 페이지 객체들을 담은 리스트를 문제의 조건대로 정렬하여 제일 앞에있는 페이지 객체의 인덱스를 반환한다.
    return sorted(all_page_objects, key=lambda x: [-x.matching_score, x.index])[0].index
