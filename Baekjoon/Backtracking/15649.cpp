#include <cstdio>
#include <algorithm>

using namespace std;

int N, M;
int result[8];
bool visited[9];

void solve(int level){

    if(level == M){
        for(int i=0; i<M; i++){
            printf("%d ", result[i]);
        }
        printf("\n");
        return;
    }

    for(int i=1; i<=N; i++){
        if(visited[i] == false){
            visited[i] = true;
            result[level] = i;
            solve(level + 1);
            visited[i] = false;
        }
    }
}


int main(void){

    fill_n(visited, 9, false);
    
    scanf("%d %d", &N, &M);
    
    solve(0);

    return 0;
}