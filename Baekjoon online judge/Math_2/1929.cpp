#include <cstdio>
#include <vector>

using namespace std;

int main(void){

    vector<int> prime_bool_v(1000001, 1);

    prime_bool_v[0]=0;
    prime_bool_v[1]=0;

    for(int i=2;i<=1000000;i++){
        if(prime_bool_v[i]==1){
            for(int j=i;j<=1000000;j+=i){

            if(j==i)
                continue;
            else if((j%i)==0 && prime_bool_v[j]==1){
                prime_bool_v[j]=0;
                }
            }
        }
        
    }

    int M, N;
    scanf("%d %d", &M, &N);

    for(int i=M;i<=N;i++){
        if(prime_bool_v[i]==1)
            printf("%d\n", i);
    }

    return 0;
}