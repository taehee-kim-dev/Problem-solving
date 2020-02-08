#include <cstdio>
#include <vector>

using namespace std;

int main(void){

    vector<int> prime_bool_v(2469124, 1);

    prime_bool_v[0]=0;
    prime_bool_v[1]=0;

    for(int i=2;i<=2469123;i++){
        if(prime_bool_v[i]==1){
            for(int j=i;j<=2469123;j+=i){

            if(j==i)
                continue;
            else if((j%i)==0 && prime_bool_v[j]==1){
                prime_bool_v[j]=0;
                }
            }
        }
        
    }

    vector<int> input_nums;

    while(true){
        int n;
        scanf("%d", &n);
        if(n==0)
            break;
        
        input_nums.push_back(n);
    }

    for(int i=0;i<input_nums.size();i++){
        int prime_count=0;
        for(int j=input_nums[i]+1;j<=2*input_nums[i];j++){
            if(prime_bool_v[j]==1){
                prime_count++;
            }
        }
        printf("%d\n", prime_count);
    }

    return 0;
}