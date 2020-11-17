#include <cstdio>
#include <vector>
#include <utility>

using namespace std;

int main(void){

    vector<int> prime_bool_vec(10000, 1);

    prime_bool_vec[0]=0;
    prime_bool_vec[1]=0;

    for(int i=2;i<prime_bool_vec.size();i++){
        if(prime_bool_vec[i]==1){
            for(int j=i;j<prime_bool_vec.size();j+=i){
                if(j==i){
                    continue;
                }else if(prime_bool_vec[j]==1){
                    prime_bool_vec[j]=0;
                }
            }
        }
    }

    int T;
    scanf("%d", &T);

    vector<pair<int, int>> result;

    while(T--){
        int input_num, left_prime, right_prime;
        scanf("%d", &input_num);
        for(int i=2;i<=input_num/2;i++){
            if(prime_bool_vec[i]==1){
                if(prime_bool_vec[input_num-i]==1){
                    left_prime=i;
                    right_prime=input_num-left_prime;
                }
            }
        }

        result.push_back(make_pair(left_prime, right_prime));
    }

    vector<pair<int, int>>::iterator iter;

    for(iter=result.begin(); iter!=result.end(); iter++){
        printf("%d %d\n", (*iter).first, (*iter).second);
    }

    return 0;
}