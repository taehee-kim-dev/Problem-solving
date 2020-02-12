#include <cstdio>
#include <cmath>

using namespace std;

int N; // 입력값
int queen_exist[16]; // 인덱스 값 = 퀸이 놓여진 행, 배열값 = 퀸이 놓여진 열 
int result = 0; // 결과값

// 매개변수로 퀸을 놓으려는 행, 열을 받음.
bool isPossible(int nextRow, int nextCol){
    // 1행부터 nextRow-1행까지 모두 검사하여
    // nextRow행 nextCol열에 퀸을 놓을 수 있는지 검사
    // 수직으로 같은 열에 있거나,
    // 대각선에 존재하면 안됨.
    for(int r=1; r <= nextRow-1; r++){
        // r이 1행부터 직전 row행까지 검사하는 인덱스
        // 수직 검사
        // r행에 퀸이 놓여져있는 열이 nextRow행에 놓으려는 열값인 nextCol값과 같으면
        // 수직으로 같은 열에 있으므로 nextRow행 nextCol열에 퀸을 놓을 수 없음.
        if(queen_exist[r] == nextCol)return false;
        // 대각선 검사
        // r행과 nextRow행의 거리와 
        // r행에서 퀸이 놓여있는 열과 nextCol열의 거리가 같으면 서로 대각선 상에 있는 것이므로
        // nextRow행 nextCol열에 퀸을 놓을 수 없음.
        if(abs(r - nextRow) == abs(queen_exist[r] - nextCol))return false;
    }

    return true;
}

// 백트래킹 함수
// 매개변수는 직전에 퀸을 놓은 행
void backTracking(int row){
    // 직전에 퀸을 놓은 행이 N이라면
    // N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 모두 놓은 것이므로
    // 결과값을 1 증가시킨다
    if(row == N){
        result++;
        return;
    }
    // 다음 행의 모든 열을 검사하여
    // 퀸을 놓을 수 있는 열을 찾음.
    for(int col=1; col<=N; col++){
        // 다음 행 col열에 퀸을 놓을 수 있는지 검사
        if(isPossible(row+1, col)){
            // 가능하다면 그 자리에 퀸을 놓음
            queen_exist[row + 1] = col;
            // 그리고 다음 행 백트래킹
            backTracking(row + 1);
        }
    }
}

// 전체적인 함수
void solve(){
    // 1행의 1열부터 N열까지 반복
    for(int col=1; col<=N; col++){
        // 1행의 col열에 퀸을 놓음
        queen_exist[1] = col;
        // 열값을 매개변수로 전달하면서 백트래킹 시작
        backTracking(1);
    }
}


int main(void){

    scanf("%d", &N);

    solve();

    printf("%d", result);

    return 0;
}