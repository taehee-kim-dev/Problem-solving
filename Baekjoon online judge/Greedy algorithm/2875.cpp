#include <cstdio>

using namespace std;

int N, M, K;

// 대회 참가 팀 수
int competition_team = 0;

void solve(){
    // 일단 여학생 2명, 남학생 1명씩 모아
    // 최대한의 대회 참가 팀 수를 만든다.
    while(N-2 >= 0 && M-1 >= 0){
        N -= 2;
        M -= 1;
        competition_team += 1;
    }

    // 그 다음, K명의 인턴쉽 프로그램 참여 학생을 뽑아야 하므로,
    // 대회에 참가하지 않는 학생들이 K명 이상일 때 까지만
    // 팀을 하나씩 해체한다.
    while(N + M < K){
        competition_team -= 1;
        N += 2;
        M += 1;
    }

    printf("%d", competition_team);
}

void input(){
    scanf("%d %d %d", &N, &M, &K);
}

int main(void){

    input();
    solve();

    return 0;
}