#include <cstdio>

using namespace std;

int N;
int K;
int A[1000001];

// 결과값 동전의 최소개수
int result=0;

// 입력
void input(){
    scanf("%d %d", &N, &K);
    for(int i=0; i<N; i++){
        scanf("%d", &A[i]);
    }
}

void solve(){
    // 제일 큰 가치의 동전부터 고려
    for(int i=N-1; i>=0; i--){
        // 현재 총 가치보다는 작거나 같아야 하므로
        if(K >= A[i]){
            // 현재 고려중인 동전의 가치가
            // 남은 가치보다 작거나 같다면,
            // 그 동전으로 최대한 가치를 채움
            // 가치가 A[i]인 동전의 최대 가능 개수만큼 결과값에 더함
            result += (K / A[i]);
            // 채운 가치만큼 총 가치에서 뺌
            K %= A[i];
        }
    }

    printf("%d", result);
}

int main(void){

    input();
    solve();

    return 0;
}