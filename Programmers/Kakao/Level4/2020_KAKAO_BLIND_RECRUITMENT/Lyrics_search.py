"""
가사 검색
"""


# 노드
class Node:
    def __init__(self, parent_node, char):
        # 해당 노드의 부모노드 저장
        self.parent_node = parent_node
        # 현재 노드의 글자
        self.char = char
        # 자식노드들
        self.child_char_nodes = dict()
        # 이 노드를 기준으로 남은 글자길이별로 단어들이 몇개씩 존재하는지
        self.number_of_remain_length_from_this_node = dict()


class Trie:
    def __init__(self, root_node):
        # 루트노드 저장
        self.root_node = root_node

    # 노드 추가
    def insert_node(self, word):
        # 현재 추가하려는 글자의 부모노드
        parent_node = self.root_node
        # 현재 추가하려는 글자를 포함한 나머지 글자의 개수
        remaining_length = len(word)
        # 단어에서 한 글자씩 차례대로 꺼내서 추가
        for char in word:
            if remaining_length in parent_node.number_of_remain_length_from_this_node:
                """
                현재 추가하려는 글자를 포함한 나머지 글자의 개수가
                현재 추가하려는 글자노드의 부모노드의 남은 글자길이별 단어의 갯수에 key로 존재하면
                해당 key값의 value를 1 증가
                """
                parent_node.number_of_remain_length_from_this_node[remaining_length] += 1
            else:
                """
                존재하지 않는다면 초기값 1로 새로 추가
                """
                parent_node.number_of_remain_length_from_this_node[remaining_length] = 1

            if char not in parent_node.child_char_nodes:
                # 현재 추가하려는 글자의 노드가 부모노드의 자식노드중에 없다면
                # 새로 만들어서 자식노드에 추가
                parent_node.child_char_nodes[char] = Node(parent_node, char)

            # 부모노드를 현재 추가한 글자의 노드로 변환 (한 단계 깊이 내려감)
            parent_node = parent_node.child_char_nodes[char]
            # 남아있는 글자의 개수 1 감소
            remaining_length -= 1

    # 검색
    def search(self, query):
        # 물음표를 모두 지우고 순수한 글자만 남김
        pure_keyword = query.replace('?', '')
        # 물음표의 개수 구함
        number_of_question_mark = len(query) - len(pure_keyword)
        # 현재 검사중인 노드
        current_node = self.root_node
        # 순수한 키워드 단어의 글자를 한 글자씩 검사
        for char in pure_keyword:
            if char in current_node.child_char_nodes:
                # 만약 글자의 노드가 현재 검사중인 노드의 자식 노드에 있다면
                # 현재 노드를 해당 자식 노드로 변환 (한 단계 깊이 내려감)
                current_node = current_node.child_char_nodes[char]
            else:
                # 없다면 검색결과는 0개
                return 0

        # 순수 단어의 글자들을 모두 검색한 이후 물음표 검사 차례
        if number_of_question_mark in current_node.number_of_remain_length_from_this_node:
            """
            남은 물음표의 개수가 현재 검사중인 노드의 number_of_remain_length_from_this_node의 key값으로 존재하면
            해당 key값에 대한 value값이 검색 결과
            """
            return current_node.number_of_remain_length_from_this_node[number_of_question_mark]
        else:
            # 존재하지 않으면 검색결과는 0
            return 0


def solution(words, queries):
    answer = []
    # 정방향 트라이용 루트노드를 만든다.
    root_node_for_forward_trie = Node(None, '*')
    # 역방향 트라이용 루트노드를 만든다.
    root_node_for_reverse_trie = Node(None, '*')
    # 정방향 트라이를 만든다.
    forward_trie = Trie(root_node_for_forward_trie)
    # 역방향 트라이를 만든다.
    reverse_trie = Trie(root_node_for_reverse_trie)

    # 가사 단어를 하나씩 꺼낸다.
    for word in words:
        # 정방향 트라이에 그대로 넣는다.
        forward_trie.insert_node(word)
        # 역방향 트라이에는 단어의 순서를 뒤집어서 넣는다.
        reverse_trie.insert_node(word[-1::-1])
        # 무조건 앞이 글자, 뒤가 물음표가 되도록.

    # 검색 키워드를 하나씩 꺼낸다.
    for query in queries:
        # 만약 해당 키워드 길이와 같은 길이의 단어가 존재하지 않는다면
        if len(query) not in root_node_for_reverse_trie.number_of_remain_length_from_this_node:
            # 검색 결과는 0개
            answer.append(0)
            continue
        # 만약 키워드 전체가 물음표로 이루어져있다면
        if query.count('?') == len(query):
            # 루트 노드에서 검사
            # 전체 단어중에 키워드의 길이와 같은 길이의 단어가 있다면
            # 그 단어들이 모두 검색결과에 해당되므로,
            # 해당 길이를 갖는 단어의 개수가 검색결과
            answer.append(root_node_for_forward_trie.number_of_remain_length_from_this_node[len(query)])
        elif query.startswith('?'):
            # 키워드가 물음표로 시작한다면
            # 역방향 트라이에 키워드를 역방향으로 검색
            answer.append(reverse_trie.search(query[-1::-1]))
        else:
            # 키워드가 물음표로 시작하지 않는다면
            # 정방향 트라이에 키워드를 정방향으로 검색
            answer.append(forward_trie.search(query))

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?", "zxc??", "?????", "???", "fro??????"]))
# [3, 2, 4, 1, 0, 5, 0]
