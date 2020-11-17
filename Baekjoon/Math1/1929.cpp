#include <cstdio>
#include <vector>

using namespace std;

int main(void){

    vector<int> numbers(1000001, 1);

    numbers[0]=0;
    numbers[1]=0;

    for(int i=2;i<=1000000;i++){
        if(numbers[i]==1){
            for(int j=i+1;j<=1000000;j++){
                if(numbers[j]==0){
                    continue;
                }else if(j%i==0){
                    numbers[j]=0;
                }
            }
        }
    }

    int M, N;
    scanf("%d", &M);
    scanf("%d", &N);

    
    for(int i=M;i<=N;i++){
        if(numbers[i]==1)
            printf("%d\n", i);
    }

    

    return 0;
}