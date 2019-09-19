#include <cstdio>
#include <vector>
#include <string>

using namespace std;

int main(void){

    int N;
    scanf("%d", &N);

    vector<int> end_numbers;

    for(int i=666; i<=2700000; i++){
        string n_str = to_string(i);

        int count_consecutive_six = 0;
        for(int j=n_str.length();j>=0; j--){
            if(n_str[j]=='6'){
                count_consecutive_six++;
                if(count_consecutive_six==3){
                    end_numbers.push_back(i);
                    count_consecutive_six=0;
                    break;
                }
            }else{
                count_consecutive_six=0;
            }
        }
        if(end_numbers.size()==N){
            printf("%d", i);
            return 0;
        }
    }

    return 0;
}