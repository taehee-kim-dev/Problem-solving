#include <cstdio>
#include <algorithm>

using namespace std;

int N;
int P[1001];

void input(){
    scanf("%d", &N);
    for(int i=0; i<N; i++){
        scanf("%d", &P[i]);
    }
}

int main(void){

    input();

    sort(P, P+N);

    int time = 0;

    for(int i=0; i<N; i++)
        for(int j=0; j<=i; j++)
            time += P[j];

    printf("%d", time);

    return 0;
}