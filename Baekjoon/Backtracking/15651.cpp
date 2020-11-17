#include <cstdio>

using namespace std;

int N, M;
int result[7];

void solve(int level){
    if(level == M){
        for(int i=0; i<M; i++){
            printf("%d ", result[i]);
        }
        printf("\n");
        return;
    }

    for(int i=1; i<=N; i++){
        result[level] = i;
        solve(level + 1);
    }
}

int main(void){

    scanf("%d %d", &N, &M);

    solve(0);

    return 0;
}