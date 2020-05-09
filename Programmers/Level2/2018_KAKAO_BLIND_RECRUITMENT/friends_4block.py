def solution(height, width, board_list):
    answer = 0

    # board_list를 90도 회전시킨 새로운 리스트 new_board_list를 구한다.
    new_board_list = list(map(list, zip(*(reversed(board_list)))))

    # # 테스트 프린트
    # print("초기 블록 배열 테스트 프린트")
    # for col_line_index in range(len(new_board_list)):
    #     for height_index in range(len(new_board_list[col_line_index])):
    #         print(new_board_list[col_line_index][height_index], end=' ')
    #     print()

    # 삭제될 블록이 없을 때 까지 무한반복 한다.
    while True:

        # 일일이 검사하면서 없어질 블록의 문자 뒤에 'd'를 붙인다.
        # 가로방향 최대 인덱스 - 1 까지만 검사.
        for current_col_line_index in range(width - 1):
            # 세로방향 최대 인덱스 - 1 까지만 검사.
            for current_height_index in range(len(new_board_list[current_col_line_index]) - 1):
                # 현재 블록의 첫 번째 문자값 임시 저장
                # 현재 블록이 삭제표시되어 뒤에 'd'가 붙어있을 수 있기 때문에 첫 번째 문자값만 저장.
                current_block = new_board_list[current_col_line_index][current_height_index][0]

                # 위, 오른쪽 위 대각선, 오른쪽 블록이 존재하고, 각 블록의 첫 번째 문자가 현재 블록의 값과 같다면
                # 해당 블록들을 지워야 하므로,
                # 블록의 길이가 1이라면 값 뒤에 'd' 추가
                # 아니라면 이미 뒤에 'd'가 추가되어 있으므로 그냥 놔둠.
                
                # 테스트 프린트
                # if current_col_line_index == 4 and current_height_index == 4:
                #     print("current_block : ", current_block)
                #     print("new_board_list[current_col_line_index][current_height_index][0] : ",
                #           new_board_list[current_col_line_index][current_height_index][0])
                #     print("new_board_list[current_col_line_index][current_height_index + 1][0] : ",
                #           new_board_list[current_col_line_index][current_height_index + 1][0])
                #     print("new_board_list[current_col_line_index + 1][current_height_index][0] : ",
                #           new_board_list[current_col_line_index + 1][current_height_index][0])
                #     print("new_board_list[current_col_line_index + 1][current_height_index + 1][0] : ",
                #           new_board_list[current_col_line_index + 1][current_height_index + 1][0])
                #     print("new_board_list[current_col_line_index][current_height_index + 1][0] == current_block : ", new_board_list[current_col_line_index][current_height_index + 1][0] == current_block)
                #     print("len(new_board_list[current_col_line_index + 1]) - 1 >= current_height_index + 1 : ", len(new_board_list[current_col_line_index + 1]) - 1 >= current_height_index + 1)
                #     print("new_board_list[current_col_line_index + 1][current_height_index + 1] == current_block : ", new_board_list[current_col_line_index + 1][current_height_index + 1][0] == current_block)
                #     print("new_board_list[current_col_line_index + 1][current_height_index] == current_block : ", new_board_list[current_col_line_index + 1][current_height_index][0] == current_block)

                if (
                        # 위 블록 검사
                        # 위 for문에서 세로방향 최대 인덱스 - 1 까지만 검사했으므로, 위 블록은 항상 존재한다.
                        # 위 블록의 첫 번째 문자값이 현재 블록의 첫 번째 문자값과 같아야 한다.
                        new_board_list[current_col_line_index][current_height_index + 1][0] == current_block

                        # 오른쪽 위 대각선 블록 검사
                        # 오른쪽 위 대각선 블록은 존재하지 않을 수 있다.
                        # 따라서, 존재여부를 파악한다.
                        and len(new_board_list[current_col_line_index + 1]) - 1 >= current_height_index + 1
                        # 오른쪽 위 대각선 블록의 첫 번째 문자값이 현재 블록의 첫 번째 문자값과 같아야 한다.
                        and new_board_list[current_col_line_index + 1][current_height_index + 1][0] == current_block

                        # 오른쪽 블록 검사
                        # 오른쪽 위 대각선 블록이 존재한다면 오른쪽 블록은 당연히 존재한다.
                        # 오른쪽 블록의 첫 번째 문자값이 현재 블록의 첫 번째 문자값과 같아야 한다.
                        and new_board_list[current_col_line_index + 1][current_height_index][0] == current_block
                ):


                    # 위의 조건문이 만족했다면, 해당 블록들을 모두 삭제표시 해야한다.

                    # 단, 현재 블록은 문자열의 길이가 1일 때 'd'를 추가해야 한다.
                    # 아래줄 검사에서 삭제표시처리가 됐을 수 있기 때문이다.
                    if len(new_board_list[current_col_line_index][current_height_index]) == 1:
                        new_board_list[current_col_line_index][current_height_index] \
                            = new_board_list[current_col_line_index][current_height_index] + 'd'

                    # 오른쪽 블록도 마찬가지이다.
                    if len(new_board_list[current_col_line_index + 1][current_height_index]) == 1:
                        new_board_list[current_col_line_index + 1][current_height_index] \
                            = new_board_list[current_col_line_index + 1][current_height_index] + 'd'

                    # 위 블록도 마찬가지이다.
                    if len(new_board_list[current_col_line_index][current_height_index + 1]) == 1:
                        new_board_list[current_col_line_index][current_height_index + 1] \
                            = new_board_list[current_col_line_index][current_height_index + 1] + 'd'

                    # 으론쪽 위 대각선 블록은 삭제표시처리가 미리 될 수 없으므로 무조건 'd'를 추가해야 한다.
                    new_board_list[current_col_line_index + 1][current_height_index + 1] \
                        = new_board_list[current_col_line_index + 1][current_height_index + 1] + 'd'
                    
            # # 테스트 프린트
            # # 세로 모두 검사 후
            # print(new_board_list)
            # print("세로 모두 검사 후 블록 배열")
            # for col_line_index in range(len(new_board_list)):
            #     for height_index in range(len(new_board_list[col_line_index])):
            #         print(new_board_list[col_line_index][height_index], end=' ')
            #     print()

        # 모든 블록들에 대한 삭제여부 체크가 끝났다.
        # 이제 모든 블록을 검사하면서,
        # 삭제체크가 된 블록들을 지우고, 삭제된 블록의 총 개수인 answer의 값을 1씩 증가시킨다.

        # 삭제 처리를 했는지 여부
        is_deleted = False

        for col_line_list_index in range(len(new_board_list)):
            before_len = len(new_board_list[col_line_list_index])
            new_col_line_list_after_delete = list(block for block in new_board_list[col_line_list_index] if len(block) == 1)
            new_board_list[col_line_list_index] = new_col_line_list_after_delete
            after_len = len(new_col_line_list_after_delete)
            len_diff = before_len - after_len
            if len_diff > 0:
                answer += len_diff
                is_deleted = True
        
        # # 테스트 프린트
        # print("삭제 처리 후 블록 배열 테스트 프린트")
        # for col_line_index in range(len(new_board_list)):
        #     for height_index in range(len(new_board_list[col_line_index])):
        #         print(new_board_list[col_line_index][height_index], end=' ')
        #     print()

        # 만약 for문을 빠져나와 지금 이 라인으로 왔는데,
        # is_deleted값이 False라면, 블록들 중에 삭제될 블록이 하나도 없다는 뜻이다.
        # 따라서 answer값을 return하면서 종료한다.

        if not is_deleted:
            return answer


print(solution(6, 6, ["QWQWBB",
                "QWQWBB",
                "AAQWBB",
                "AAQWQW",
                "QWQWQW",
                "QWQWQW"]))
