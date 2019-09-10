#include <cstdio>
#include <vector>

using namespace std;

int main(void){

    int M, N;

    scanf("%d", &M);
    scanf("%d", &N);

    vector<int> nums(10001, 1);

    nums[0]=0;
    nums[1]=0;

    int i=2;
    while(i<=10000){
        while(nums[i]==0){
            i++;
        }

        for(int j=i;j<=10000;j+=i){
            if(j==i || nums[j]==0)
                continue;
            else{
                nums[j]=0;
            }
        }
        i++;
    }

    vector<int> primes;

    int lowest=0;

    for(int k=M;k<=N;k++){
        if(nums[k]==1){
            primes.push_back(k);
        }
    }

    int sum=0;
    for(int v=0;v<primes.size();v++){
        sum+=primes[v];
    }

    if(primes.empty()){
        printf("%d", -1);
    }else{
        printf("%d\n%d", sum, primes[0]);
    }

    return 0;
}