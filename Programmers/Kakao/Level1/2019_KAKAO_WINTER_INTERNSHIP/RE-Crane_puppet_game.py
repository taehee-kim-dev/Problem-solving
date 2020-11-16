"""
2019 카카오 개발자 겨울 인턴십
크레인 인형뽑기 게임
"""


def solution(board, moves):
    answer = 0

    basket = []
    for move in moves:
        for row in range(0, len(board)):
            if board[row][move - 1] > 0:
                if basket and basket[-1] == board[row][move - 1]:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(board[row][move - 1])
                board[row][move - 1] = 0
                break
    return answer
