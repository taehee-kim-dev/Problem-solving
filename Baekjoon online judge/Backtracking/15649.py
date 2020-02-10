import sys

def solve(level): # 매개변수 = 트리 레벨

    if level == M:  # 트리의 레벨이 M과 같아지면 result list 모두 출력
        for i in result:
            print(i, end=' ') # 공백구분

        print() # result list 모두 출력하고 개행
        return

    else:
        for i in range(1, N+1): # 1부터 N까지 한 레벨
            if not visited[i]: # i번째 숫자를 선택 안했다면,
                visited[i] = True # 선택으로 바꾸고,
                result.append(i) # 결과 리스트에 i를 append
                solve(level + 1) # 다음 레벨의 노드들 탐색
                '''
                다음 레벨을 탐색하는 함수에서 리턴되었을 때,
                다음 레벨에서 현재 레벨로 돌아왔으므로 visited 리스트에서 
                선택했던 숫자에 대한 boolean값을 True에서 False로 변경
                그리고 result list에서 맨 뒷값 제거
                '''
                visited[i] = False
                result.pop()
                # 그리고 다음 노드를 검사함


N, M = map(int, sys.stdin.readline().split())

visited = [False for _ in range(N+1)]
result = []

solve(0)

