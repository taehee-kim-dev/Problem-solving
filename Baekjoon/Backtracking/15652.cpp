#include <cstdio>

using namespace std;

int N, M;
int result[8];

void solve(int level, int min){
    if(level == M){
        for(int i=0; i<M; i++){
            printf("%d ", result[i]);
        }
        printf("\n");
        return;
    }

    for(int i=min; i<=N; i++){
        result[level] = i;
        solve(level + 1, i);
    }
}

int main(void){

    scanf("%d %d", &N, &M);

    solve(0, 1);

    return 0;
}