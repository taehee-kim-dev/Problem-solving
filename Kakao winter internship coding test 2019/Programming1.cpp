#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    // board : 게임화면 격자 상태 (5x5) ~ (30x30)
    // index 0 = moves값 1
    // 0 : 빈 칸
    // 1~100 : 인형의 종류
    
    // moves : 크레인을 작동시킨 위치(좌우 가로 위치) 1 ~ 1000
    
    // answer : 크레인을 모두 작동시킨 후 터뜨려져 사라진 인형의 갯수
    int answer = 0;
    // 인형을 담을 바구니 basket vector
    vector<int> basket;
    // 정사각형 board격자 한 변의 크기
    int board_size = board.size();

    // turn = 크레인 작동 턴
    for(int turn=0; turn<moves.size(); turn++){
        // 크레인이 board의 맨 위에서부터 내려감
        for(int depth=0; depth<board_size; depth++){
            // 인형이 있으면
            if(board[depth][moves[turn]-1]!=0){
                // 인형
                int doll = board[depth][moves[turn]-1];

                if(basket.size()>0 && basket.back() == doll){
                    answer+=2;
                    basket.pop_back();
                }else{
                    basket.push_back(doll);
                }

                // board에서 인형 위치의 값을 0으로 업데이트
                board[depth][moves[turn]-1]=0;
                break;
            }
        }
    }

    return answer;
}

int main(void){

    vector<vector<int>> board = {{0,0,0,0,0},{0,0,1,0,3},{0,2,5,0,1},{4,2,4,4,2},{3,5,1,3,1}};
    vector<int> moves = {1,5,3,5,1,2,1,4};

    printf("%d", solution(board, moves));

    return 0;
}