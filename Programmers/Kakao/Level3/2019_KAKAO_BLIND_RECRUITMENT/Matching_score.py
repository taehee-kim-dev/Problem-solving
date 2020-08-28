"""
매칭 점수
"""

import re
from decimal import Decimal


class WebPage:
    def __init__(self, index, content):
        # 인덱스
        self.index = index
        # 자기 자신의 주소
        self.own_link = ''
        # 내용
        self.content = content
        # 기본점수 : 검색어 등장 횟수
        self.basic_score = Decimal('0')
        # 외부 링크
        self.external_links = []
        # 외부 링크 수 : 다른 외부 링크 개수
        self.number_of_external_links = Decimal('0')
        # 링크점수 : (이 웹페이지를 참조하는 외부 페이지의 기본점수 / 이 웹페이지를 참조하는 외부 페이지의 외부 링크 수)의 총합
        self.link_score = Decimal('0')
        # 매칭점수 : 기본점수 + 링크점수
        self.matching_score = Decimal('0')


def get_word_search_count(page_object, word):
    body_tag = re.search('<body>.*</body>', page_object.content, re.DOTALL)
    return len(re.findall('[^a-zA-Z]+' + word + '[^a-zA-Z]+', body_tag.group(), re.IGNORECASE))


def get_own_link(page_object):
    meta_tag = re.search('<meta property="og:url" content="https://(.*)"/*>', page_object.content)
    return meta_tag.groups()[0]


def get_external_links(page_object):
    body_tag = re.search('<body>.*</body>', page_object.content, re.DOTALL)
    return re.findall('<a href="https://(.*)">', body_tag.group())


def solution(word, pages):
    web_page_objects = []

    for index, page in enumerate(pages):
        web_page_objects.append(WebPage(index, page))

    for page_object in web_page_objects:
        page_object.basic_score = Decimal(str(get_word_search_count(page_object, word)))
        page_object.own_link = get_own_link(page_object)
        page_object.external_links = get_external_links(page_object)
        page_object.number_of_external_links = Decimal(len(page_object.external_links))

    for page_object in web_page_objects:
        page_objects_referencing_this_page = [page for page in web_page_objects if page_object.own_link in page.external_links]
        link_score = Decimal('0')
        for referencing_page_object in page_objects_referencing_this_page:
            link_score += Decimal(str(referencing_page_object.basic_score)) / Decimal(str(referencing_page_object.number_of_external_links))
        page_object.link_score = link_score
        page_object.matching_score = page_object.basic_score + page_object.link_score

    return sorted(web_page_objects, key=lambda x: [-x.matching_score, x.index])[0].index


print(solution('blind', [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
# 0

print(solution('Muzi', [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
# 1
