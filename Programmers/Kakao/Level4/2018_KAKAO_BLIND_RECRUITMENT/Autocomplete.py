"""
[3차] 자동완성
"""

# 정답 전역변수
answer = 0


# 글자 노드
class CharNode:
    def __init__(self, char, word_length):
        # 글자값
        self.char = char
        # 이 글자노드를 갖는 단어의 개수
        self.number_of_words_with_this_char = 0
        # 단어 첫 번째 글자부터 이 노드까지의 길이
        self.word_length = word_length
        # 자식노드들
        self.child_nodes = dict()
        # 이 글자노드가 어떤 단어의 끝에 해당하는가?
        self.is_terminal = False


# 트라이
class Trie:
    def __init__(self, root_node):
        # 루트노드 설정
        self.root_node = root_node

    # 단어 삽입 함수
    def insert_word(self, word):
        # 초기 부모노드는 루트노드
        parent_node = self.root_node
        # 단어의 글자 하나씩 순서대로 삽입
        for index, char in enumerate(word):
            if char not in parent_node.child_nodes:
                # 만약 글자에 해당하는 노드가
                # 부모노드의 자식노드들중에 없으면
                # 새로 만들어서 추가한다.
                # 만드는 글자노드의 단어 처음부터의 길이는 부모노드의 해당 값 + 1
                parent_node.child_nodes[char] = CharNode(char, parent_node.word_length + 1)
            # 해당 글자노드를 갖는 단어의 개수를 1 증가
            parent_node.child_nodes[char].number_of_words_with_this_char += 1
            if index == len(word) - 1:
                # 만약 현재 글자가 단어의 마지막 글자라면
                # 해당 글자노드에 어떤 단어의 끝임을 표시
                parent_node.child_nodes[char].is_terminal = True
            # 부모노드를 현재 처리한 자식노드로 바꿈
            parent_node = parent_node.child_nodes[char]

    # 정답 찾기 함수
    def find_answer(self, node):
        # 전역변수 answer 수정 선언
        global answer
        if node.number_of_words_with_this_char == 1:
            # 현재 노드를 갖는 단어가 1개라면
            # 정답값을 현재 글자노드의 단어 처음부터의 길이값을 더하고 리턴
            answer += node.word_length
            return
        else:
            # 현재 노드를 갖는 단어가 2개 이상이라면
            if node.is_terminal:
                # 현재 노드가 어떤 단어의 끝이라면
                # 정답을 현재 노드의 길이만큼 더한다.
                answer += node.word_length

            # 현재 노드의 자식노드들을 재귀함수로 호출하여 검사
            for child_node in node.child_nodes.values():
                self.find_answer(child_node)


def solution(words):
    # 전역변수 수정 선언
    global answer

    # 루트노드 생성
    root_node = CharNode(None, 0)
    # 루트노드를 생성자 매개변수로 하여 트라이 생성
    trie = Trie(root_node)

    # 단어를 하나씩 꺼냄
    for word in words:
        # 트라이에 삽입
        trie.insert_word(word)

    # 매 테스트케이스 실행마다 전역변수 이전 결과값이 영향을 끼치므로
    # 0으로 초기화
    answer = 0
    # 답 찾기
    trie.find_answer(root_node)
    # 정답값 반환
    return answer


print(solution(['go', 'gone', 'guild']))
# 7

print(solution(['abc', 'def', 'ghi', 'jklm']))
# 4

print(solution(['word', 'war', 'warrior', 'world']))
# 15
