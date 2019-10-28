#include <cstdio>
#include <vector>

using namespace std;

int main(void){

    int N;

    scanf("%d", &N);

    vector<vector<int>> case_of_numbers(N+1, vector<int>(10, 0));

    for(int last_num=1; last_num<=9; last_num++)
        case_of_numbers[1][last_num]=1;

    for(int length=2; length<=N; length++){
        for(int last_num=0; last_num<=9; last_num++){

            if(last_num==0)
                case_of_numbers[length][last_num] = case_of_numbers[length-1][last_num+1]%1000000000;
            else if(last_num==9)
                case_of_numbers[length][last_num] = case_of_numbers[length-1][last_num-1]%1000000000;
            else
                case_of_numbers[length][last_num] = (case_of_numbers[length-1][last_num-1] + case_of_numbers[length-1][last_num+1])%1000000000;
        }
    }

    int result=0;
    for(int last_num=0; last_num<=9; last_num++)
        result = (result + case_of_numbers[N][last_num])%1000000000;

    printf("%d", result);

    return 0;
}